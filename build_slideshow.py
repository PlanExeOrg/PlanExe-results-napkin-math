"""Build snapshot/46/slideshow.html from every assessment.md in snapshot/46/."""

from __future__ import annotations

import html
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

SNAPSHOT_DIR = Path(__file__).parent / "snapshot" / "46"
OUTPUT_PATH = SNAPSHOT_DIR / "slideshow.html"

VERDICT_COLORS = {
    "ROBUST": "#2e7d32",
    "MARGINAL": "#f9a825",
    "FRAGILE": "#ef6c00",
    "DOOM": "#c62828",
    "UNKNOWN": "#616161",
}
BAND_LABEL = {
    "viable": "VIABLE",
    "marginal": "MARGINAL",
    "fragile": "FRAGILE",
    "doom": "DOOM",
    "unknown": "UNKNOWN",
}
BAND_COLOR = {
    "viable": VERDICT_COLORS["ROBUST"],
    "marginal": VERDICT_COLORS["MARGINAL"],
    "fragile": VERDICT_COLORS["FRAGILE"],
    "doom": VERDICT_COLORS["DOOM"],
    "unknown": VERDICT_COLORS["UNKNOWN"],
}


@dataclass
class Gate:
    name: str
    pass_rate: float  # 0..1
    verdict: str
    threshold_basis: str = ""


@dataclass
class Driver:
    gate: str
    top_driver: str
    delta_pp: str
    pass_requires: str


@dataclass
class UnmodelledGate:
    name: str
    why: str


@dataclass
class DeckStats:
    total_plans: int
    band_counts: dict[str, int]
    total_declared_gates: int
    total_failed_gates: int
    total_unmodelled: int


@dataclass
class Plan:
    slug: str
    name: str
    plan_type: str
    primary_goal: str
    overall_band: str
    worst_gate: str
    worst_pass_rate: float
    failed_gates: list[str]
    uncertainty_drivers: list[str]
    unmodelled_gate_names: list[str]
    gate_verdicts: list[Gate] = field(default_factory=list)
    failure_drivers: list[Driver] = field(default_factory=list)
    unmodelled_gates: list[UnmodelledGate] = field(default_factory=list)
    next_actions: list[str] = field(default_factory=list)


# ---------- parsing ----------


def extract_section(md: str, header: str) -> str:
    """Return body of `## header` up to the next `## ` line."""
    pattern = rf"^## {re.escape(header)}\n(.*?)(?=^## |\Z)"
    m = re.search(pattern, md, flags=re.MULTILINE | re.DOTALL)
    return m.group(1).strip() if m else ""


def extract_json_block(md: str) -> dict:
    m = re.search(r"```json\n(\{.*?\n\})\n```", md, flags=re.DOTALL)
    return json.loads(m.group(1)) if m else {}


def extract_primary_goal(md: str) -> tuple[str, str]:
    """Return (plan_type, primary_goal) from the header block."""
    type_m = re.search(r"\*\*Type:\*\*\s*(\S+)", md)
    goal_m = re.search(r"\*\*Primary goal:\*\*\s*(.+?)(?=\n##|\n\n)", md, flags=re.DOTALL)
    plan_type = type_m.group(1).strip() if type_m else ""
    goal = goal_m.group(1).strip().replace("\n", " ") if goal_m else ""
    return plan_type, goal


def parse_md_table(section: str) -> list[list[str]]:
    """Parse first markdown table in the section into list of row-cell-lists."""
    rows: list[list[str]] = []
    lines = [ln for ln in section.splitlines() if ln.strip().startswith("|")]
    for ln in lines:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        rows.append(cells)
    if len(rows) < 2:
        return []
    # rows[0] header, rows[1] separator, rows[2:] data
    return [rows[0]] + rows[2:]


def parse_pct(text: str) -> float:
    m = re.search(r"([\d.]+)\s*%", text)
    return float(m.group(1)) / 100.0 if m else 0.0


def strip_md_inline(text: str) -> str:
    """Remove backticks, bold markers, and HTML-escape."""
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\*\*([^*]*)\*\*", r"\1", text)
    return text.strip()


def parse_assessment(slug: str, md_path: Path) -> Plan:
    md = md_path.read_text(encoding="utf-8")
    info = extract_json_block(md)
    plan_type, goal = extract_primary_goal(md)

    pmr = info.get("primary_model_result", {})

    # Gate verdicts table
    gates: list[Gate] = []
    gv_section = extract_section(md, "Gate verdicts")
    table = parse_md_table(gv_section)
    if table:
        header = table[0]
        # header: ['', 'Output', 'Condition', 'Threshold basis', 'Pass rate', 'Verdict', 'Meaning']
        try:
            idx_out = header.index("Output")
            idx_pr = header.index("Pass rate")
            idx_vd = header.index("Verdict")
            idx_tb = header.index("Threshold basis")
        except ValueError:
            idx_out, idx_tb, idx_pr, idx_vd = 1, 3, 4, 5
        for row in table[1:]:
            if len(row) <= idx_vd:
                continue
            name = strip_md_inline(row[idx_out])
            if not name:
                continue
            pr = parse_pct(row[idx_pr])
            vd = strip_md_inline(row[idx_vd]).upper()
            tb = strip_md_inline(row[idx_tb])
            gates.append(Gate(name=name, pass_rate=pr, verdict=vd, threshold_basis=tb))

    # Failure drivers table
    drivers: list[Driver] = []
    fd_section = extract_section(md, "Failure drivers")
    table = parse_md_table(fd_section)
    if table:
        for row in table[1:]:
            if len(row) < 4:
                continue
            drivers.append(
                Driver(
                    gate=strip_md_inline(row[0]),
                    top_driver=strip_md_inline(row[1]),
                    delta_pp=strip_md_inline(row[2]),
                    pass_requires=strip_md_inline(row[3]),
                )
            )

    # Unmodelled existential gates table
    unmodelled: list[UnmodelledGate] = []
    um_section = extract_section(md, "Known unmodelled existential gates")
    table = parse_md_table(um_section)
    if table:
        for row in table[1:]:
            if len(row) < 2:
                continue
            unmodelled.append(
                UnmodelledGate(
                    name=strip_md_inline(row[0]),
                    why=strip_md_inline(row[1]),
                )
            )

    # Suggested next actions — numbered list
    actions: list[str] = []
    sa_section = extract_section(md, "Suggested next actions")
    for ln in sa_section.splitlines():
        m = re.match(r"\s*\d+\.\s+(.+)", ln)
        if m:
            actions.append(strip_md_inline(m.group(1)))

    return Plan(
        slug=slug,
        name=info.get("plan_name", slug),
        plan_type=plan_type,
        primary_goal=goal,
        overall_band=pmr.get("overall_risk_band", "unknown"),
        worst_gate=pmr.get("worst_gate", ""),
        worst_pass_rate=pmr.get("worst_gate_pass_rate", 0.0),
        failed_gates=info.get("primary_failed_gates", []),
        uncertainty_drivers=info.get("primary_uncertainty_drivers", []),
        unmodelled_gate_names=info.get("known_unmodelled_existential_gates", []),
        gate_verdicts=gates,
        failure_drivers=drivers,
        unmodelled_gates=unmodelled,
        next_actions=actions,
    )


# ---------- rendering ----------


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def render_gate_bar_chart(gates: list[Gate]) -> str:
    """Inline SVG horizontal bar chart, threshold lines at 20/50/80."""
    if not gates:
        return '<p class="muted">No gate data.</p>'
    n = len(gates)
    row_h = 44
    label_w = 320
    chart_w = 560
    pad_top = 32
    pad_bottom = 28
    total_h = pad_top + n * row_h + pad_bottom
    total_w = label_w + chart_w + 80

    threshold_lines = []
    for pct, label in [(20, "DOOM"), (50, "FRAGILE"), (80, "MARGINAL/ROBUST")]:
        x = label_w + (pct / 100) * chart_w
        threshold_lines.append(
            f'<line x1="{x:.1f}" y1="{pad_top - 6}" x2="{x:.1f}" y2="{pad_top + n * row_h + 2}" '
            f'stroke="#bbb" stroke-dasharray="3 3" stroke-width="1"/>'
            f'<text x="{x:.1f}" y="{pad_top - 12}" font-size="10" fill="#666" text-anchor="middle">{pct}%</text>'
        )

    bars = []
    for i, g in enumerate(gates):
        y = pad_top + i * row_h
        bar_w = max(2.0, g.pass_rate * chart_w)
        color = VERDICT_COLORS.get(g.verdict, "#999")
        label = esc(g.name)
        verdict_label = esc(g.verdict)
        pct_label = f"{g.pass_rate * 100:.1f}%"
        bars.append(
            f'<text x="{label_w - 10}" y="{y + row_h / 2 + 5}" font-size="13" font-family="ui-monospace, monospace" '
            f'fill="#222" text-anchor="end">{label}</text>'
            f'<rect x="{label_w}" y="{y + 8}" width="{bar_w:.1f}" height="{row_h - 16}" fill="{color}" '
            f'rx="3" ry="3"/>'
            f'<text x="{label_w + bar_w + 8:.1f}" y="{y + row_h / 2 + 5}" font-size="13" fill="#222">'
            f'{pct_label} <tspan fill="{color}" font-weight="600">{verdict_label}</tspan></text>'
        )

    # x-axis baseline
    axis = (
        f'<line x1="{label_w}" y1="{pad_top + n * row_h + 4}" '
        f'x2="{label_w + chart_w}" y2="{pad_top + n * row_h + 4}" stroke="#444" stroke-width="1"/>'
    )

    return (
        f'<svg viewBox="0 0 {total_w} {total_h}" width="100%" '
        f'preserveAspectRatio="xMidYMid meet" role="img" aria-label="Gate pass rates">'
        + "".join(threshold_lines)
        + axis
        + "".join(bars)
        + "</svg>"
    )


def render_verdict_badge(band: str, worst_gate: str, worst_pr: float) -> str:
    color = BAND_COLOR.get(band, "#666")
    label = BAND_LABEL.get(band, band.upper())
    pct = f"{worst_pr * 100:.1f}%" if worst_pr is not None else "—"
    return (
        f'<div class="verdict" style="background:{color};">'
        f'<div class="verdict-label">OVERALL</div>'
        f'<div class="verdict-band">{esc(label)}</div>'
        f'<div class="verdict-sub">worst gate: <code>{esc(worst_gate or "n/a")}</code></div>'
        f'<div class="verdict-sub">pass rate: <strong>{pct}</strong></div>'
        f"</div>"
    )


def compute_stats(plans: list[Plan]) -> DeckStats:
    counts: dict[str, int] = {"doom": 0, "fragile": 0, "marginal": 0, "viable": 0}
    for p in plans:
        key = p.overall_band if p.overall_band in counts else "unknown"
        counts[key] = counts.get(key, 0) + 1
    return DeckStats(
        total_plans=len(plans),
        band_counts=counts,
        total_declared_gates=sum(len(p.gate_verdicts) for p in plans),
        total_failed_gates=sum(len(p.failed_gates) for p in plans),
        total_unmodelled=sum(len(p.unmodelled_gate_names) for p in plans),
    )


def render_band_bar_chart(band_counts: dict[str, int]) -> str:
    bands = [("doom", "DOOM", "<20%"), ("fragile", "FRAGILE", "20–50%"),
             ("marginal", "MARGINAL", "50–80%"), ("viable", "ROBUST", "≥80%")]
    total = sum(band_counts.values()) or 1
    max_count = max(max(band_counts.values()), 1)
    chart_w, chart_h = 760, 360
    pad_top, pad_bottom, pad_l, pad_r = 56, 88, 60, 30
    plot_w = chart_w - pad_l - pad_r
    plot_h = chart_h - pad_top - pad_bottom
    slot = plot_w / len(bands)
    bar_w = slot * 0.58

    # Y-axis grid lines at integer counts
    grid = []
    for n in range(max_count + 1):
        y = pad_top + plot_h - (n / max_count) * plot_h
        grid.append(
            f'<line x1="{pad_l}" y1="{y:.1f}" x2="{pad_l + plot_w:.1f}" y2="{y:.1f}" '
            f'stroke="#eee" stroke-width="1"/>'
        )
        grid.append(
            f'<text x="{pad_l - 8}" y="{y + 4:.1f}" font-size="11" fill="#999" '
            f'text-anchor="end" font-variant-numeric="tabular-nums">{n}</text>'
        )

    bars = []
    for i, (key, label, thresh) in enumerate(bands):
        count = band_counts.get(key, 0)
        h = (count / max_count) * plot_h if count > 0 else 0
        cx = pad_l + i * slot + slot / 2
        x = cx - bar_w / 2
        y = pad_top + plot_h - h
        color = BAND_COLOR.get(key, "#666")
        pct = count / total * 100
        if count > 0:
            bars.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" '
                        f'height="{h:.1f}" fill="{color}" rx="3"/>')
        else:
            # tiny stub so zero is visible
            bars.append(f'<rect x="{x:.1f}" y="{pad_top + plot_h - 2:.1f}" '
                        f'width="{bar_w:.1f}" height="2" fill="{color}" opacity="0.25"/>')
        bars.append(
            f'<text x="{cx:.1f}" y="{max(y - 12, pad_top + 14):.1f}" font-size="28" '
            f'font-weight="700" fill="#222" text-anchor="middle">{count}</text>'
        )
        bars.append(
            f'<text x="{cx:.1f}" y="{max(y - 36, pad_top - 4):.1f}" font-size="12" '
            f'fill="#666" text-anchor="middle">{pct:.0f}%</text>'
        )
        bars.append(
            f'<text x="{cx:.1f}" y="{pad_top + plot_h + 26:.1f}" font-size="14" '
            f'font-weight="600" fill="{color}" text-anchor="middle">{label}</text>'
        )
        bars.append(
            f'<text x="{cx:.1f}" y="{pad_top + plot_h + 46:.1f}" font-size="11" '
            f'fill="#888" text-anchor="middle">pass rate {thresh}</text>'
        )

    baseline = (f'<line x1="{pad_l}" y1="{pad_top + plot_h:.1f}" '
                f'x2="{pad_l + plot_w:.1f}" y2="{pad_top + plot_h:.1f}" stroke="#444" stroke-width="1.5"/>')

    return (f'<svg viewBox="0 0 {chart_w} {chart_h}" width="100%" '
            f'preserveAspectRatio="xMidYMid meet" role="img" aria-label="Plans per verdict band">'
            + "".join(grid) + "".join(bars) + baseline + "</svg>")


def intro_slide_headline(stats: DeckStats) -> str:
    return f"""
<section class="slide">
  <header class="slide-head">
    <div class="kicker">PlanExe &middot; snapshot 46</div>
    <h1>Napkin-math assessment overview</h1>
    <p class="lede">Monte-Carlo viability stress tests for each plan. Pass rates are taken over 10,000 simulated runs per declared gate; verdict bands: DOOM &lt;20%, FRAGILE 20–50%, MARGINAL 50–80%, ROBUST ≥80%. Each plan is profiled across the three slides that follow this overview.</p>
  </header>
  <div class="intro-metrics">
    <div class="big-metric"><div class="bm-num">{stats.total_plans}</div><div class="bm-cap">plans assessed</div></div>
    <div class="big-metric"><div class="bm-num">{stats.total_declared_gates}</div><div class="bm-cap">declared gates total</div></div>
    <div class="big-metric"><div class="bm-num">{stats.total_failed_gates}</div><div class="bm-cap">failed gates (DOOM or FRAGILE)</div></div>
    <div class="big-metric warn"><div class="bm-num">{stats.total_unmodelled}</div><div class="bm-cap">unmodelled existential gates</div></div>
  </div>
  <footer class="slide-foot"><span>Overview 1 / 3 &middot; headline figures</span></footer>
</section>
"""


def intro_slide_distribution(stats: DeckStats) -> str:
    chart = render_band_bar_chart(stats.band_counts)
    doom = stats.band_counts.get("doom", 0)
    frag = stats.band_counts.get("fragile", 0)
    marg = stats.band_counts.get("marginal", 0)
    viab = stats.band_counts.get("viable", 0)
    summary = (f"<strong>{doom}</strong> DOOM, <strong>{frag}</strong> FRAGILE, "
               f"<strong>{marg}</strong> MARGINAL, <strong>{viab}</strong> ROBUST")
    return f"""
<section class="slide">
  <header class="slide-head">
    <div class="kicker">Snapshot 46 &middot; verdict distribution</div>
    <h1>How many plans are doomed?</h1>
    <p class="lede">Each plan's overall risk band is set by its worst declared gate. {summary} of {stats.total_plans} plans.</p>
  </header>
  <div class="chart-wrap big">
    {chart}
  </div>
  <footer class="slide-foot"><span>Overview 2 / 3 &middot; verdict band distribution</span></footer>
</section>
"""


def intro_slide_roster(plans: list[Plan]) -> str:
    sorted_plans = sorted(plans, key=lambda p: (p.worst_pass_rate, p.slug))
    rows = []
    for p in sorted_plans:
        band = BAND_LABEL.get(p.overall_band, p.overall_band.upper())
        color = BAND_COLOR.get(p.overall_band, "#666")
        pct = p.worst_pass_rate * 100
        rows.append(
            f"<tr>"
            f"<td class='plan-cell'>"
            f"<div class='plan-name'>{esc(p.name)}</div>"
            f"<code class='plan-slug'>{esc(p.slug)}</code>"
            f"</td>"
            f"<td><span class='band-pill' style='background:{color}'>{esc(band)}</span></td>"
            f"<td class='num'>{pct:.1f}%</td>"
            f"<td class='bar-cell'>"
            f"<div class='mini-bar'><div class='mini-bar-fill' "
            f"style='width:{max(pct, 0.5):.1f}%;background:{color}'></div></div>"
            f"</td>"
            f"<td><code class='wg'>{esc(p.worst_gate)}</code></td>"
            f"</tr>"
        )
    return f"""
<section class="slide">
  <header class="slide-head">
    <div class="kicker">Snapshot 46 &middot; plan roster</div>
    <h1>Plans ranked by worst-gate pass rate</h1>
    <p class="lede">Most doomed at the top. The bar shows the worst gate's pass rate; the verdict band is determined by where that pass rate falls.</p>
  </header>
  <table class="roster">
    <thead><tr>
      <th>Plan</th><th>Band</th><th>Worst pass rate</th><th>Visualization</th><th>Worst gate</th>
    </tr></thead>
    <tbody>{''.join(rows)}</tbody>
  </table>
  <footer class="slide-foot"><span>Overview 3 / 3 &middot; plan roster</span></footer>
</section>
"""


def slide_overview(plan: Plan) -> str:
    badge = render_verdict_badge(plan.overall_band, plan.worst_gate, plan.worst_pass_rate)
    failed_n = len(plan.failed_gates)
    unmod_n = len(plan.unmodelled_gate_names)
    return f"""
<section class="slide">
  <header class="slide-head">
    <div class="kicker">{esc(plan.slug)} &middot; {esc(plan.plan_type)}</div>
    <h1>{esc(plan.name)}</h1>
  </header>
  <div class="overview">
    <div class="goal">
      <h3>Primary goal</h3>
      <p>{esc(plan.primary_goal)}</p>
      <div class="metric-row">
        <div class="metric"><span class="metric-num">{failed_n}</span><span class="metric-cap">failed gates</span></div>
        <div class="metric"><span class="metric-num">{unmod_n}</span><span class="metric-cap">unmodelled existential gates</span></div>
        <div class="metric"><span class="metric-num">{len(plan.gate_verdicts)}</span><span class="metric-cap">declared gates</span></div>
      </div>
    </div>
    {badge}
  </div>
  <footer class="slide-foot"><span>Slide 1 / 3 &middot; overview &amp; verdict</span></footer>
</section>
"""


def slide_gate_chart(plan: Plan) -> str:
    chart = render_gate_bar_chart(plan.gate_verdicts)
    # Legend
    legend = """
    <div class="legend">
      <span><span class="sw" style="background:#c62828"></span>DOOM &lt;20%</span>
      <span><span class="sw" style="background:#ef6c00"></span>FRAGILE 20–50%</span>
      <span><span class="sw" style="background:#f9a825"></span>MARGINAL 50–80%</span>
      <span><span class="sw" style="background:#2e7d32"></span>ROBUST ≥80%</span>
    </div>
    """
    return f"""
<section class="slide">
  <header class="slide-head">
    <div class="kicker">{esc(plan.slug)}</div>
    <h1>Gate pass rates</h1>
    <p class="lede">Pass rate per declared gate over 10,000 Monte-Carlo runs. Verdict band determined by pass rate.</p>
  </header>
  <div class="chart-wrap">
    {chart}
  </div>
  {legend}
  <footer class="slide-foot"><span>Slide 2 / 3 &middot; gate pass rates</span></footer>
</section>
"""


def slide_drivers(plan: Plan) -> str:
    # Failure drivers
    if plan.failure_drivers:
        drv_rows = "".join(
            f"<tr><td><code>{esc(d.gate)}</code></td><td><code>{esc(d.top_driver)}</code></td>"
            f"<td class='num'>{esc(d.delta_pp)}</td><td>{esc(d.pass_requires)}</td></tr>"
            for d in plan.failure_drivers
        )
        drv_table = f"""
        <table class="data-table">
          <thead><tr><th>Failing gate</th><th>Top driver</th><th>Δ-pp</th><th>80% pass requires</th></tr></thead>
          <tbody>{drv_rows}</tbody>
        </table>"""
    else:
        drv_table = '<p class="muted">No failing gates — nothing to drive.</p>'

    # Unmodelled gates
    if plan.unmodelled_gates:
        um_items = "".join(
            f"<li><code>{esc(g.name)}</code><div class='um-why'>{esc(g.why[:280] + ('…' if len(g.why) > 280 else ''))}</div></li>"
            for g in plan.unmodelled_gates
        )
        um_block = f"<ul class='um-list'>{um_items}</ul>"
    else:
        um_block = '<p class="muted">No unmodelled existential gates flagged.</p>'

    return f"""
<section class="slide">
  <header class="slide-head">
    <div class="kicker">{esc(plan.slug)}</div>
    <h1>Drivers &amp; out-of-model risks</h1>
  </header>
  <div class="drivers-grid">
    <div class="panel">
      <h3>Failure drivers (modelled)</h3>
      {drv_table}
    </div>
    <div class="panel warn">
      <h3>Unmodelled existential gates</h3>
      <p class="muted small">The simulation does not test these. Treat all modelled pass rates as conditional on them holding.</p>
      {um_block}
    </div>
  </div>
  <footer class="slide-foot"><span>Slide 3 / 3 &middot; drivers &amp; out-of-model risks</span></footer>
</section>
"""


CSS = """
:root {
  --bg: #f5f5f4;
  --slide-bg: #ffffff;
  --ink: #1c1c1c;
  --muted: #6b6b6b;
  --rule: #e5e5e3;
  --kicker: #888;
}
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: var(--bg); color: var(--ink);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif; }
.deck { position: relative; }
.slide {
  width: min(1100px, 96vw);
  min-height: 88vh;
  margin: 24px auto;
  background: var(--slide-bg);
  border-radius: 6px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.08), 0 8px 24px rgba(0,0,0,0.06);
  padding: 38px 48px 32px;
  display: none;
  flex-direction: column;
  scroll-margin-top: 16px;
}
.slide.active { display: flex; }
.slide-head { border-bottom: 1px solid var(--rule); padding-bottom: 16px; margin-bottom: 22px; }
.slide-head .kicker {
  font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--kicker); font-family: ui-monospace, "SF Mono", Menlo, monospace;
}
.slide-head h1 { font-size: 28px; margin: 6px 0 0; font-weight: 600; line-height: 1.25; }
.slide-head .lede { color: var(--muted); margin: 8px 0 0; font-size: 14px; max-width: 70ch; }
.slide-foot {
  margin-top: auto; padding-top: 18px; border-top: 1px solid var(--rule);
  color: var(--muted); font-size: 11px; font-family: ui-monospace, monospace;
  letter-spacing: 0.06em; text-transform: uppercase;
}

/* Overview slide */
.overview { display: grid; grid-template-columns: 1.5fr 1fr; gap: 32px; align-items: start; }
.goal h3 { margin: 0 0 8px; font-size: 12px; text-transform: uppercase; letter-spacing: 0.1em; color: var(--muted); }
.goal p { margin: 0; font-size: 16px; line-height: 1.55; }
.metric-row { margin-top: 28px; display: flex; gap: 24px; }
.metric { display: flex; flex-direction: column; }
.metric-num { font-size: 32px; font-weight: 600; line-height: 1; }
.metric-cap { font-size: 11px; color: var(--muted); text-transform: uppercase; letter-spacing: 0.08em; margin-top: 6px; }
.verdict {
  color: white; padding: 24px; border-radius: 6px; display: flex; flex-direction: column;
  align-items: flex-start; min-height: 200px;
}
.verdict-label { font-size: 11px; letter-spacing: 0.12em; opacity: 0.85; }
.verdict-band { font-size: 56px; font-weight: 700; line-height: 1; margin: 8px 0 18px; letter-spacing: -0.01em; }
.verdict-sub { font-size: 13px; margin-top: 4px; opacity: 0.95; }
.verdict-sub code { background: rgba(255,255,255,0.18); padding: 1px 6px; border-radius: 3px; }

/* Chart slide */
.chart-wrap { padding: 8px 0; }
.legend { display: flex; flex-wrap: wrap; gap: 18px; font-size: 12px; color: var(--muted); margin-top: 8px; }
.legend .sw { display: inline-block; width: 12px; height: 12px; border-radius: 2px; vertical-align: middle; margin-right: 6px; }

/* Intro slides */
.intro-metrics {
  display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; margin-top: 28px;
}
.big-metric {
  padding: 22px 22px 20px; background: #fafaf8; border-radius: 6px;
  border: 1px solid var(--rule);
}
.big-metric.warn { background: #fff7f0; border-color: #ef6c00; }
.bm-num { font-size: 46px; font-weight: 700; line-height: 1; }
.bm-cap {
  font-size: 11px; color: var(--muted); text-transform: uppercase;
  letter-spacing: 0.08em; margin-top: 12px;
}
.chart-wrap.big { padding: 18px 0 8px; }
.roster { width: 100%; border-collapse: collapse; font-size: 13px; margin-top: 8px; }
.roster th, .roster td {
  padding: 9px 10px; border-bottom: 1px solid var(--rule);
  text-align: left; vertical-align: middle;
}
.roster th {
  font-size: 10px; text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--muted); font-weight: 600;
}
.roster td.plan-cell { line-height: 1.3; }
.roster .plan-name { font-weight: 500; font-size: 13px; color: var(--ink); }
.roster .plan-slug { font-size: 10.5px; color: var(--muted); display: block; margin-top: 2px; }
.roster td.num { text-align: right; font-variant-numeric: tabular-nums; font-weight: 600; }
.roster td.bar-cell { width: 220px; }
.roster .wg { font-size: 11px; }
.band-pill {
  display: inline-block; padding: 3px 10px; border-radius: 12px;
  color: white; font-size: 10px; font-weight: 700; letter-spacing: 0.06em;
}
.mini-bar { width: 100%; height: 10px; background: var(--rule); border-radius: 5px; overflow: hidden; }
.mini-bar-fill { height: 100%; }

/* Drivers slide */
.drivers-grid { display: flex; flex-direction: column; gap: 22px; }
.panel h3 { margin: 0 0 12px; font-size: 13px; text-transform: uppercase; letter-spacing: 0.1em; color: var(--ink); }
.panel.warn h3 { color: #b3300f; }
.panel.warn { background: #fff7f0; border: 1px solid #ef6c00; border-left-width: 3px; padding: 14px 18px 16px; border-radius: 0 4px 4px 0; }
.data-table { width: 100%; border-collapse: collapse; font-size: 12px; }
.data-table th, .data-table td {
  text-align: left; padding: 6px 8px; border-bottom: 1px solid var(--rule); vertical-align: top;
}
.data-table th { font-weight: 600; color: var(--muted); text-transform: uppercase; font-size: 10px; letter-spacing: 0.08em; }
.data-table td.num { text-align: right; font-variant-numeric: tabular-nums; }
.um-list { list-style: none; padding: 0; margin: 0; }
.um-list li { margin-bottom: 14px; }
.um-why { color: var(--muted); font-size: 12px; line-height: 1.5; margin-top: 3px; }
code { font-family: ui-monospace, "SF Mono", Menlo, monospace; font-size: 0.92em; }
.muted { color: var(--muted); }
.small { font-size: 12px; }

/* Nav bar */
.nav {
  position: fixed; bottom: 0; left: 0; right: 0; background: rgba(255,255,255,0.96);
  border-top: 1px solid var(--rule); padding: 10px 16px; display: flex;
  align-items: center; gap: 12px; backdrop-filter: blur(6px); z-index: 10;
}
.nav button {
  border: 1px solid var(--rule); background: white; padding: 6px 12px; border-radius: 4px;
  font-size: 13px; cursor: pointer; font-family: inherit;
}
.nav button:hover { background: #f1f1ef; }
.nav .progress { flex: 1; height: 4px; background: var(--rule); border-radius: 2px; overflow: hidden; }
.nav .progress > div { height: 100%; background: var(--ink); transition: width 0.18s; }
.nav .counter { font-size: 12px; color: var(--muted); font-variant-numeric: tabular-nums; min-width: 80px; text-align: center; }
.nav select {
  border: 1px solid var(--rule); background: white; padding: 5px 8px; border-radius: 4px;
  font-size: 12px; font-family: inherit; max-width: 320px;
}
.help { font-size: 11px; color: var(--muted); }
"""

JS = r"""
const INTRO_SLIDES = 3;
const PER_PLAN = 3;
const slides = Array.from(document.querySelectorAll('.slide'));
const counter = document.getElementById('counter');
const progress = document.getElementById('progress-bar');
const select = document.getElementById('plan-select');
let idx = 0;
function show(i) {
  idx = Math.max(0, Math.min(slides.length - 1, i));
  slides.forEach((s, k) => s.classList.toggle('active', k === idx));
  counter.textContent = (idx + 1) + ' / ' + slides.length;
  progress.style.width = ((idx + 1) / slides.length * 100) + '%';
  let targetSelectIdx;
  if (idx < INTRO_SLIDES) {
    targetSelectIdx = 0;
  } else {
    targetSelectIdx = Math.floor((idx - INTRO_SLIDES) / PER_PLAN) + 1;
  }
  if (select.selectedIndex !== targetSelectIdx) select.selectedIndex = targetSelectIdx;
  history.replaceState(null, '', '#s' + (idx + 1));
}
document.getElementById('prev').addEventListener('click', () => show(idx - 1));
document.getElementById('next').addEventListener('click', () => show(idx + 1));
select.addEventListener('change', (e) => {
  const si = e.target.selectedIndex;
  show(si === 0 ? 0 : INTRO_SLIDES + (si - 1) * PER_PLAN);
});
document.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') { e.preventDefault(); show(idx + 1); }
  else if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); show(idx - 1); }
  else if (e.key === 'Home') { e.preventDefault(); show(0); }
  else if (e.key === 'End') { e.preventDefault(); show(slides.length - 1); }
});
// hash-based deep link on load
const m = (location.hash || '').match(/^#s(\d+)$/);
show(m ? parseInt(m[1], 10) - 1 : 0);
"""


def render_html(plans: list[Plan]) -> str:
    stats = compute_stats(plans)
    slides_html = [
        intro_slide_headline(stats),
        intro_slide_distribution(stats),
        intro_slide_roster(plans),
    ]
    options = ['<option value="overview">— Overview —</option>']
    for i, plan in enumerate(plans):
        slides_html.append(slide_overview(plan))
        slides_html.append(slide_gate_chart(plan))
        slides_html.append(slide_drivers(plan))
        band_label = BAND_LABEL.get(plan.overall_band, plan.overall_band.upper())
        options.append(
            f'<option value="{i}">{esc(plan.slug)} — {esc(plan.name)} [{esc(band_label)}]</option>'
        )

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>PlanExe snapshot 46 — assessment slideshow</title>
<style>{CSS}</style>
</head>
<body>
<div class="deck">
{''.join(slides_html)}
</div>
<div class="nav">
  <button id="prev" aria-label="Previous slide">← Prev</button>
  <button id="next" aria-label="Next slide">Next →</button>
  <select id="plan-select" aria-label="Jump to plan">
    {''.join(options)}
  </select>
  <span class="counter" id="counter">1 / {3 + len(plans) * 3}</span>
  <div class="progress"><div id="progress-bar" style="width:0%"></div></div>
  <span class="help">← / → keys</span>
</div>
<script>{JS}</script>
</body>
</html>
"""


def main() -> None:
    plan_dirs = sorted(
        d for d in SNAPSHOT_DIR.iterdir()
        if d.is_dir() and (d / "assessment.md").exists()
    )
    plans = [parse_assessment(d.name, d / "assessment.md") for d in plan_dirs]
    OUTPUT_PATH.write_text(render_html(plans), encoding="utf-8")
    total = 3 + len(plans) * 3
    print(f"Wrote {OUTPUT_PATH}: 3 overview + {len(plans)} plans × 3 = {total} slides.")


if __name__ == "__main__":
    main()
