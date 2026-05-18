"""Build snapshot/46/slideshow.html from every assessment.md in snapshot/46/."""

from __future__ import annotations

import html
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from methodology_slides import MethodologySlide, extract_slides

SNAPSHOT_DIR = Path(__file__).parent / "snapshot" / "46"
OUTPUT_PATH = SNAPSHOT_DIR / "slideshow.html"
METHODOLOGY_PATH = SNAPSHOT_DIR / "methology.md"

INTRO_SLIDES = 9
PER_PLAN = 6

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
    confidence_grade: str = ""  # LOW / MEDIUM / HIGH / "" — from montecarlo.json/model_confidence


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
    consequence: str = ""
    source_anchor: str = ""


@dataclass
class MissingInput:
    rank: int
    input_id: str
    worst_gate: str
    score: float
    bound_width_ratio: float
    source: str  # e.g. "assumption", "data" — from montecarlo.json/missing_value_priority[i].source


@dataclass
class ScenarioRow:
    """Output values at deterministic low/base/high input scenarios."""
    low: float | None
    base: float | None
    high: float | None
    unit: str


@dataclass
class GateCondition:
    operator: str  # ">=", ">", "<=", "<", "=="
    value: float


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
    missing_inputs: list[MissingInput] = field(default_factory=list)
    scenarios: dict[str, ScenarioRow] = field(default_factory=dict)
    gate_conditions: dict[str, GateCondition] = field(default_factory=dict)
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


def _maybe_float(v) -> float | None:
    if v is None:
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


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

    # Unmodelled existential gates — read from parameters.json for the
    # consequence_if_false field (which the assessment.md table renders but
    # the parameters file is the source of truth).
    unmodelled: list[UnmodelledGate] = []
    params_path = md_path.parent / "parameters.json"
    if params_path.exists():
        params = json.loads(params_path.read_text(encoding="utf-8"))
        for um_entry in params.get("unmodelled_gates", []):
            unmodelled.append(UnmodelledGate(
                name=um_entry.get("id", ""),
                why=um_entry.get("why_it_matters", ""),
                consequence=um_entry.get("consequence_if_false", ""),
                source_anchor=um_entry.get("source_anchor", ""),
            ))

    # Suggested next actions — numbered list
    actions: list[str] = []
    sa_section = extract_section(md, "Suggested next actions")
    for ln in sa_section.splitlines():
        m = re.match(r"\s*\d+\.\s+(.+)", ln)
        if m:
            actions.append(strip_md_inline(m.group(1)))

    # Raw simulation data — pulled directly from JSON, not from the markdown.
    missing_inputs: list[MissingInput] = []
    gate_conditions: dict[str, GateCondition] = {}
    mc_path = md_path.parent / "montecarlo.json"
    output_units: dict[str, str] = {}
    if mc_path.exists():
        mc = json.loads(mc_path.read_text(encoding="utf-8"))
        for rank, entry in enumerate(mc.get("missing_value_priority", []), start=1):
            missing_inputs.append(MissingInput(
                rank=rank,
                input_id=entry.get("id", ""),
                worst_gate=entry.get("worst_gate", ""),
                score=float(entry.get("score", 0.0)),
                bound_width_ratio=float(entry.get("bound_width_ratio", 0.0)),
                source=entry.get("source", ""),
            ))
        for gname, th in mc.get("thresholds", {}).items():
            gate_conditions[gname] = GateCondition(
                operator=str(th.get("operator", ">=")),
                value=float(th.get("value", 0.0)),
            )
        for gname, out in mc.get("outputs", {}).items():
            unit = out.get("unit") if isinstance(out, dict) else None
            if unit:
                output_units[gname] = unit
        # Populate per-gate confidence grade by mutating already-parsed `gates`.
        # IMPORTANT: don't shadow the outer `info` variable (the assessment JSON
        # block) — that regression once silently emptied plan_name / failed_gates
        # / unmodelled_gate_names for every plan.
        mc_conf = mc.get("model_confidence", {})
        if isinstance(mc_conf, dict):
            for g in gates:
                conf_entry = mc_conf.get(g.name)
                if isinstance(conf_entry, dict):
                    grade = conf_entry.get("grade")
                    if isinstance(grade, str):
                        g.confidence_grade = grade.upper()

    scenarios: dict[str, ScenarioRow] = {}
    sc_path = md_path.parent / "scenarios.json"
    if sc_path.exists():
        sc = json.loads(sc_path.read_text(encoding="utf-8"))
        sc_data = sc.get("scenarios", {}) if isinstance(sc, dict) else {}
        low_out = sc_data.get("low", {}).get("outputs", {}) if isinstance(sc_data, dict) else {}
        base_out = sc_data.get("base", {}).get("outputs", {}) if isinstance(sc_data, dict) else {}
        high_out = sc_data.get("high", {}).get("outputs", {}) if isinstance(sc_data, dict) else {}
        gate_names = set(low_out) | set(base_out) | set(high_out)
        for gname in gate_names:
            scenarios[gname] = ScenarioRow(
                low=_maybe_float(low_out.get(gname)),
                base=_maybe_float(base_out.get(gname)),
                high=_maybe_float(high_out.get(gname)),
                unit=output_units.get(gname, ""),
            )

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
        missing_inputs=missing_inputs,
        scenarios=scenarios,
        gate_conditions=gate_conditions,
        next_actions=actions,
    )


# ---------- rendering ----------


def esc(text: str) -> str:
    return html.escape(text, quote=True)


# Suffix tokens that are units — stripped from gate IDs for short labels.
# Ordered longest-first so multi-token units are stripped before their suffixes.
_UNIT_SUFFIXES = (
    "persons_per_km2", "hours_per_week", "hours_per_month",
    "per_week", "per_month", "per_day", "per_year", "per_crate",
    "milliseconds", "seconds", "minutes", "tonnes", "persons",
    "hours", "days", "months", "weeks", "years", "ms", "kbps", "mbps", "gbps",
    "inr", "usd", "eur", "dkk", "gbp", "jpy", "cny",
    "share", "fraction", "pct", "ratio", "count", "units", "pp", "tons",
    "kg", "kwh", "mwh", "mw", "gw", "km2", "bps",
)

# Tokens that should be rendered uppercase as recognized acronyms.
_ACRONYMS = {
    "mttr", "mtbf", "pue", "fid", "opex", "capex", "kpi", "roi", "ev",
    "opc", "ua", "mou", "rte", "anssi", "dgsi", "nsc", "eci",
    "tld", "icann", "gsa", "doi", "aml", "osha", "io", "api", "p99",
    "uk", "us", "eu", "dkk", "usd", "eur", "inr", "ai", "ml",
    "c2", "n95", "hsm", "emc", "mos", "drf", "milstd", "noi",
}


def short_gate_label(gate_id: str) -> str:
    """Compact, human-readable label from a snake_case gate ID.

    Strips trailing unit tokens (e.g. `_hours`, `_inr`) and a final
    `_margin`, then renders acronyms in uppercase. Full ID is preserved
    elsewhere (detail table, SVG <title>, aria-label).
    """
    s = (gate_id or "").lower()
    # Strip unit suffix tokens (greedy, in case multiple stack)
    changed = True
    while changed:
        changed = False
        for u in _UNIT_SUFFIXES:
            suffix = "_" + u
            if s.endswith(suffix):
                s = s[: -len(suffix)]
                changed = True
                break
    # Strip trailing `_margin`
    if s.endswith("_margin"):
        s = s[: -len("_margin")]
    if not s:
        return gate_id
    tokens = s.split("_")
    out: list[str] = []
    for t in tokens:
        if t in _ACRONYMS:
            out.append(t.upper())
        elif t.startswith("phase") and t[5:].isdigit():
            out.append("Phase " + t[5:])
        elif t.startswith("year") and t[4:].isdigit():
            out.append("Year " + t[4:])
        else:
            out.append(t)
    return " ".join(out)


def render_gate_bar_chart(gates: list[Gate]) -> str:
    """Inline SVG horizontal bar chart, threshold lines at 20/50/80.

    Uses short labels in the chart for readability; full gate IDs are kept
    in the SVG <title> element (browser tooltip) and aria-label.
    """
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
    for pct in (20, 50, 80):
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
        short = esc(short_gate_label(g.name))
        full_id = esc(g.name)
        verdict_label = esc(g.verdict)
        pct_label = f"{g.pass_rate * 100:.1f}%"
        # Wrap the whole row in a <g> with a <title> so hovering shows the full
        # gate ID as a native browser tooltip.
        bars.append(
            f'<g aria-label="{full_id}"><title>{full_id}</title>'
            f'<text x="{label_w - 10}" y="{y + row_h / 2 + 5}" font-size="13" '
            f'font-family="-apple-system, BlinkMacSystemFont, system-ui, sans-serif" '
            f'fill="#222" text-anchor="end">{short}</text>'
            f'<rect x="{label_w}" y="{y + 8}" width="{bar_w:.1f}" height="{row_h - 16}" fill="{color}" '
            f'rx="3" ry="3"/>'
            f'<text x="{label_w + bar_w + 8:.1f}" y="{y + row_h / 2 + 5}" font-size="13" fill="#222">'
            f'{pct_label} <tspan fill="{color}" font-weight="600">{verdict_label}</tspan></text>'
            f'</g>'
        )

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


def render_verdict_badge(
    band: str, worst_gate: str, worst_pr: float,
    n_unmodelled: int = 0, unmodelled_heavy: bool = False,
) -> str:
    color = BAND_COLOR.get(band, "#666")
    label = BAND_LABEL.get(band, band.upper())
    pct = f"{worst_pr * 100:.1f}%" if worst_pr is not None else "—"

    if n_unmodelled == 0:
        caveat_html = (
            '<div class="verdict-caveat">'
            'Not a whole-plan probability &mdash; the verdict reflects the worst declared gate.'
            '</div>'
        )
    else:
        gate_word = "gate" if n_unmodelled == 1 else "gates"
        heavy_html = (
            '<div class="verdict-caveat-headline">Unmodelled-heavy &mdash; '
            'verdict is highly conditional.</div>' if unmodelled_heavy else ''
        )
        caveat_html = (
            f'<div class="verdict-caveat">'
            f'{heavy_html}'
            f'Conditional on {n_unmodelled} unmodelled existential {gate_word} holding. '
            f'Not a whole-plan probability.'
            f'</div>'
        )

    return (
        f'<div class="verdict" style="background:{color};">'
        f'<div class="verdict-label">VERDICT</div>'
        f'<div class="verdict-band">{esc(label)}</div>'
        f'<div class="verdict-sub">worst gate: <code>{esc(worst_gate or "n/a")}</code></div>'
        f'<div class="verdict-sub">pass rate: <strong>{pct}</strong></div>'
        f'{caveat_html}'
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
    chart_w, chart_h = 760, 380
    pad_top, pad_bottom, pad_l, pad_r = 70, 88, 60, 30
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
        # Label baseline: 12px above bar top, but clamped so the ascender
        # (~22px for 24px font) doesn't fall off the top of the SVG.
        label_y = max(y - 12, 30)
        bars.append(
            f'<text x="{cx:.1f}" y="{label_y:.1f}" font-size="24" '
            f'font-weight="700" fill="#222" text-anchor="middle">'
            f'{count} <tspan font-size="14" font-weight="500" fill="#666">'
            f'({pct:.0f}%)</tspan></text>'
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


def render_distribution_strip(band_counts: dict[str, int], total: int) -> str:
    bands = [("doom", "DOOM"), ("fragile", "FRAGILE"),
             ("marginal", "MARGINAL"), ("viable", "ROBUST")]
    total = total or 1
    segments = []
    for key, label in bands:
        count = band_counts.get(key, 0)
        if count == 0:
            continue
        pct = count / total * 100
        color = BAND_COLOR.get(key, "#666")
        segments.append(
            f'<div class="strip-seg" style="background:{color};flex:{count};">'
            f'<div class="strip-label">{esc(label)}</div>'
            f'<div class="strip-count">{count}<span class="strip-pct">({pct:.0f}%)</span></div>'
            f"</div>"
        )
    return f'<div class="dist-strip">{"".join(segments)}</div>'


def intro_slide_headline(stats: DeckStats) -> str:
    strip = render_distribution_strip(stats.band_counts, stats.total_plans)
    return f"""
<section class="slide title-slide">
  <header class="slide-head">
    <div class="kicker">PlanExe</div>
    <h1>Napkin-math overview</h1>
  </header>
  {strip}
  <div class="intro-metrics">
    <div class="big-metric"><div class="bm-num">{stats.total_plans}</div><div class="bm-cap">plans assessed</div></div>
    <div class="big-metric"><div class="bm-num">{stats.total_declared_gates}</div><div class="bm-cap">declared gates total</div></div>
    <div class="big-metric"><div class="bm-num">{stats.total_failed_gates}</div><div class="bm-cap">failed gates (DOOM or FRAGILE)</div></div>
    <div class="big-metric"><div class="bm-num">{stats.total_unmodelled}</div><div class="bm-cap">unmodelled existential gates</div></div>
  </div>
  <footer class="slide-foot"><span>Overview 1 / 9 &middot; headline figures</span></footer>
</section>
"""


def intro_slide_distribution(stats: DeckStats) -> str:
    chart = render_band_bar_chart(stats.band_counts)
    return f"""
<section class="slide">
  <header class="slide-head">
    <div class="kicker">verdict distribution</div>
    <h1>How many plans are doomed?</h1>
    <p class="lede">Each plan's overall risk band is set by its worst declared gate.</p>
  </header>
  <div class="chart-wrap big">
    {chart}
  </div>
  <footer class="slide-foot"><span>Overview 2 / 9 &middot; verdict band distribution</span></footer>
</section>
"""


def _base_case_cell(plan: Plan) -> str:
    """Render the 'Base case' roster cell for a plan: pass/fail badge + value."""
    cond = plan.gate_conditions.get(plan.worst_gate)
    sc = plan.scenarios.get(plan.worst_gate)
    if sc is None or sc.base is None or cond is None:
        return "<td class='base-cell'><span class='muted'>—</span></td>"
    val_str, val_cls = _format_scenario_value(sc.base, cond)
    if "pass" in val_cls:
        pf_label, pf_cls = "PASS", "pf-pass"
    elif "fail" in val_cls:
        pf_label, pf_cls = "FAIL", "pf-fail"
    else:
        pf_label, pf_cls = "?", "pf-unknown"
    unit_span = (
        f"<span class='base-unit'>{esc(sc.unit)}</span>" if sc.unit else ""
    )
    return (
        f"<td class='base-cell'>"
        f"<span class='pass-fail {pf_cls}'>{pf_label}</span>"
        f"<span class='base-val'>{esc(val_str)}</span>"
        f"{unit_span}"
        f"</td>"
    )


def intro_slide_roster(plans: list[Plan]) -> str:
    indexed = list(enumerate(plans))
    sorted_indexed = sorted(indexed, key=lambda ip: (ip[1].worst_pass_rate, ip[1].slug))
    rows = []
    for orig_idx, p in sorted_indexed:
        band = BAND_LABEL.get(p.overall_band, p.overall_band.upper())
        color = BAND_COLOR.get(p.overall_band, "#666")
        pct = p.worst_pass_rate * 100
        target_slide = INTRO_SLIDES + orig_idx * PER_PLAN  # 0-based
        base_cell = _base_case_cell(p)
        rows.append(
            f"<tr class='roster-row' data-target='{target_slide}' "
            f"tabindex='0' role='link' "
            f"aria-label='Jump to {esc(p.name)}'>"
            f"<td class='plan-cell'>"
            f"<div class='plan-name'>{esc(p.name)}</div>"
            f"<code class='plan-slug'>{esc(p.slug)}</code>"
            f"</td>"
            f"<td><span class='band-pill' style='background:{color}'>{esc(band)}</span></td>"
            f"{base_cell}"
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
    <div class="kicker">plan roster</div>
    <h1>Plans ranked by worst-gate pass rate</h1>
    <p class="lede">The &ldquo;worst gate wins&rdquo; rule is defensible, but harsh: it catches fatal bottlenecks, but it can hide whether a plan is one fix away from viability or broadly broken. A plan with one failed gate and four marginal gates is very different from a plan with five failing gates.</p>
  </header>
  <table class="roster">
    <thead><tr>
      <th>Plan</th><th>Band</th><th>Base case</th><th>Worst pass rate</th><th>Visualization</th><th>Worst gate</th>
    </tr></thead>
    <tbody>{''.join(rows)}</tbody>
  </table>
  <p class="muted small roster-footnote"><strong>Base case</strong> = the worst gate's value at the deterministic <em>base</em> input scenario. FAIL means the plan fails its own central assumptions, not only in tail cases.</p>
  <footer class="slide-foot"><span>Overview 3 / 9 &middot; plan roster</span></footer>
</section>
"""


def slide_methodology(slide: MethodologySlide, index: int, total: int) -> str:
    return f"""
<section class="slide methodology-slide">
  <header class="slide-head">
    <div class="kicker">methodology &middot; slide {esc(slide.key)}</div>
    <h1>{esc(slide.title)}</h1>
  </header>
  <div class="methodology-body">
    {slide.body_html}
  </div>
  <footer class="slide-foot"><span>Overview {index} / {total} &middot; methodology</span></footer>
</section>
"""


def per_plan_verdict_distribution(gates: list[Gate]) -> str:
    """Stacked horizontal bar showing this plan's gate-verdict distribution."""
    order = ["DOOM", "FRAGILE", "MARGINAL", "ROBUST"]
    counts = {v: 0 for v in order}
    for g in gates:
        if g.verdict in counts:
            counts[g.verdict] += 1
    if sum(counts.values()) == 0:
        return "<div class='vdist-bar empty'></div>"
    segs = []
    for v in order:
        c = counts[v]
        if c == 0:
            continue
        color = VERDICT_COLORS[v]
        title = f"{c} {v.lower()} gate{'s' if c != 1 else ''}"
        segs.append(
            f'<div class="vdist-seg" style="background:{color};flex:{c};" '
            f'title="{title}">{c}</div>'
        )
    return f'<div class="vdist-bar">{"".join(segs)}</div>'


def _evaluate_base_case(plan: Plan) -> tuple[str, str, str, str]:
    """Return (status, formatted_value, unit, gate_name) for a plan's worst gate
    at the base scenario. status ∈ {"pass", "fail", "unknown"}."""
    cond = plan.gate_conditions.get(plan.worst_gate)
    sc = plan.scenarios.get(plan.worst_gate)
    if cond is None or sc is None or sc.base is None:
        return ("unknown", "—", "", plan.worst_gate)
    formatted, css_cls = _format_scenario_value(sc.base, cond)
    if "fail" in css_cls:
        status = "fail"
    elif "pass" in css_cls:
        status = "pass"
    else:
        status = "unknown"
    return (status, formatted, sc.unit, plan.worst_gate)


def _pick_examples_by_class(items: list[tuple], k: int = 4) -> list[tuple]:
    """Pick up to k examples covering different failure classes.

    items: list of (plan, formatted_value, unit, gate) tuples.
    Returns: list of (class_label, plan, formatted_value, unit, gate) sorted
    by the most-populated class first. Within each class, picks the worst-
    pass-rate plan as the representative.
    """
    by_class: dict[str, list[tuple]] = {}
    for item in items:
        gate = item[3]
        cls = classify_gate_class(gate)
        by_class.setdefault(cls, []).append(item)
    # Order classes by how many plans fail in that class (most first), so
    # the most representative class examples come first. "Other" pushed last.
    sorted_classes = sorted(
        by_class.items(),
        key=lambda kv: (kv[0] == "Other", -len(kv[1])),
    )
    chosen: list[tuple] = []
    for cls, members in sorted_classes:
        if len(chosen) >= k:
            break
        # Within the class, pick the worst-pass-rate plan as canonical example.
        member = min(members, key=lambda x: x[0].worst_pass_rate)
        chosen.append((cls, *member))
    return chosen


def intro_slide_base_case_failure(plans: list[Plan]) -> str:
    """Cross-plan finding: which plans fail their worst gate at base inputs."""
    n_fail = 0
    n_pass = 0
    n_unknown = 0
    fail_examples: list[tuple] = []  # (plan, formatted_value, unit, gate)
    for p in plans:
        status, formatted, unit, gate = _evaluate_base_case(p)
        if status == "fail":
            n_fail += 1
            fail_examples.append((p, formatted, unit, gate))
        elif status == "pass":
            n_pass += 1
        else:
            n_unknown += 1
    total = len(plans)

    if n_fail == total and total > 0:
        headline_h1 = f"All {total} plans fail their worst gate under base inputs"
        big_num = f"{total} / {total}"
    elif total > 0:
        headline_h1 = (
            f"{n_fail} of {total} plans fail their worst gate under base inputs"
        )
        big_num = f"{n_fail} / {total}"
    else:
        headline_h1 = "No plans assessed"
        big_num = "0 / 0"

    examples = _pick_examples_by_class(fail_examples, k=4)
    if examples:
        rows = []
        for cls, plan, formatted, unit, gate in examples:
            unit_cell = (
                f"<span class='muted small'>{esc(unit)}</span>" if unit else ""
            )
            rows.append(
                f"<tr>"
                f"<td class='bc-class'>{esc(cls)}</td>"
                f"<td class='plan-cell'>"
                f"<div class='plan-name'>{esc(plan.name)}</div>"
                f"<code class='plan-slug'>{esc(plan.slug)}</code>"
                f"</td>"
                f"<td><code>{esc(short_gate_label(gate))}</code></td>"
                f"<td class='num bc-val'>{esc(formatted)}</td>"
                f"<td>{unit_cell}</td>"
                f"</tr>"
            )
        examples_html = f"""
        <h3 class="bc-section-title">One example per failure class</h3>
        <table class="roster bc-examples">
          <thead><tr>
            <th>Class</th><th>Plan</th><th>Worst gate</th>
            <th class='num'>Base value</th><th>Unit</th>
          </tr></thead>
          <tbody>{''.join(rows)}</tbody>
        </table>
        <p class='muted small'>One canonical failing plan per failure class &mdash; not a ranking. Picked as the worst-failing plan within each class.</p>"""
    else:
        examples_html = ""

    unknown_note = (
        f"<p class='muted small'>{n_unknown} plan(s) excluded — base-scenario data unavailable.</p>"
        if n_unknown > 0 else ""
    )

    return f"""
<section class="slide">
  <header class="slide-head">
    <div class="kicker">base-case finding</div>
    <h1>{esc(headline_h1)}</h1>
  </header>
  <div class="bc-headline">
    <div class="bc-num">{esc(big_num)}</div>
    <div class="bc-text">
      <strong>plans whose worst gate fails at deterministic base inputs.</strong><br>
      The Monte Carlo is not merely exposing tail risk &mdash; the central assumptions already miss at least one declared commitment in every flagged plan.
    </div>
  </div>
  {examples_html}
  {unknown_note}
  <footer class="slide-foot"><span>Overview 4 / 9 &middot; base-case failure</span></footer>
</section>
"""


def intro_slide_histogram(plans: list[Plan]) -> str:
    indexed = list(enumerate(plans))
    sorted_indexed = sorted(indexed, key=lambda ip: (ip[1].worst_pass_rate, ip[1].slug))
    rows = []
    for orig_idx, p in sorted_indexed:
        band = BAND_LABEL.get(p.overall_band, p.overall_band.upper())
        color = BAND_COLOR.get(p.overall_band, "#666")
        target_slide = INTRO_SLIDES + orig_idx * PER_PLAN
        bar = per_plan_verdict_distribution(p.gate_verdicts)
        n_gates = len(p.gate_verdicts)
        n_drivers = len(p.failure_drivers)
        n_unmodelled = len(p.unmodelled_gate_names)
        rows.append(
            f"<tr class='roster-row' data-target='{target_slide}' "
            f"tabindex='0' role='link' "
            f"aria-label='Jump to {esc(p.name)}'>"
            f"<td class='plan-cell'>"
            f"<div class='plan-name'>{esc(p.name)}</div>"
            f"<code class='plan-slug'>{esc(p.slug)}</code>"
            f"</td>"
            f"<td><span class='band-pill' style='background:{color}'>{esc(band)}</span></td>"
            f"<td class='num'>{n_gates}</td>"
            f"<td class='vdist-cell'>{bar}</td>"
            f"<td class='num'>{n_drivers}</td>"
            f"<td class='num warn-num'>{n_unmodelled}</td>"
            f"</tr>"
        )
    legend = (
        '<div class="legend">'
        '<span><span class="sw" style="background:#c62828"></span>DOOM &lt;20%</span>'
        '<span><span class="sw" style="background:#ef6c00"></span>FRAGILE 20–50%</span>'
        '<span><span class="sw" style="background:#f9a825"></span>MARGINAL 50–80%</span>'
        '<span><span class="sw" style="background:#2e7d32"></span>ROBUST ≥80%</span>'
        '</div>'
    )
    return f"""
<section class="slide">
  <header class="slide-head">
    <div class="kicker">gate verdicts by plan</div>
    <h1>Gate verdicts by plan</h1>
    <p class="lede">Each row's bar shows how that plan's declared gates distribute across verdict bands.</p>
  </header>
  {legend}
  <table class="roster">
    <thead><tr>
      <th>Plan</th><th>Overall</th><th>Gates</th><th>Gate verdict distribution</th>
      <th class='num'>Failure drivers</th><th class='num'>Unmodelled gates</th>
    </tr></thead>
    <tbody>{''.join(rows)}</tbody>
  </table>
  <footer class="slide-foot"><span>Overview 9 / 9 &middot; gate verdicts by plan</span></footer>
</section>
"""


# Failure-class keyword groups. First-match-wins on a gate ID's tokens.
# Order matters — more specific / financial categories first so that gates
# like `monthly_off_peak_rental_overhead_margin_dkk` land in Budget rather
# than Operations (matched on `overhead`).
_FAILURE_CLASSES: list[tuple[str, tuple[str, ...]]] = [
    ("Budget / margin", (
        "budget", "surplus", "overrun", "capex", "opex", "funding",
        "donation", "noi", "float", "cash", "drf", "milstd", "rental",
        "cost", "profitability_trigger", "profitability",
    )),
    ("Governance / regulatory", (
        "compliance", "regulatory", "cert", "license", "authorization",
        "aml", "zone_zero", "deficit",
    )),
    ("Market / adoption", (
        "adoption", "conversion", "sellthrough", "awareness", "participation",
        "social_impressions", "impressions", "registration", "presale",
        "taster", "referendum", "support",
    )),
    ("Schedule / timing", (
        "timing", "publish", "deadline", "window", "timeline", "delegation",
    )),
    ("Technical integration", (
        "api", "bid", "mos", "kbps", "protocol", "fieldbus", "integration",
        "fid",
    )),
    ("Operations / throughput", (
        "uptime", "mttr", "throughput", "intervention", "audit", "endurance",
        "coverage", "density", "pue", "staging", "recovery", "verification",
        "productivity", "complaint", "overhead", "review_load", "latency",
        "mtbf",
    )),
]


def classify_gate_class(gate_id: str) -> str:
    """Return a failure-class label for a gate ID. First-match-wins."""
    s = (gate_id or "").lower()
    for label, keywords in _FAILURE_CLASSES:
        for k in keywords:
            if k in s:
                return label
    return "Other"


def _plan_short_name(p: Plan) -> str:
    """Compact display name for a plan — strip trailing parens, truncate."""
    name = re.sub(r"\s*\([^)]*\)\s*$", "", p.name or "").strip() or p.slug
    return name if len(name) <= 32 else name[:29].rstrip() + "…"


def intro_slide_failure_clustering(plans: list[Plan]) -> str:
    """Cross-plan synthesis: every failing gate grouped by category."""
    # Collect every failing gate together with its plan.
    failing: list[tuple[Plan, Gate]] = []
    for p in plans:
        for g in p.gate_verdicts:
            if g.verdict in ("DOOM", "FRAGILE"):
                failing.append((p, g))

    # Bucket by class.
    by_class: dict[str, list[tuple[Plan, Gate]]] = {
        label: [] for label, _ in _FAILURE_CLASSES
    }
    by_class["Other"] = []
    for p, g in failing:
        cls = classify_gate_class(g.name)
        by_class.setdefault(cls, []).append((p, g))

    # Sort categories: largest count first, "Other" last.
    sorted_classes = sorted(
        by_class.items(),
        key=lambda kv: (kv[0] == "Other", -len(kv[1])),
    )

    total_failing = len(failing)
    rows = []
    for cls_label, members in sorted_classes:
        if not members:
            continue
        # Up to 4 example gate+plan pairs (worst-failing first).
        members_sorted = sorted(members, key=lambda pg: pg[1].pass_rate)[:4]
        examples_html = ", ".join(
            f"<span class='fc-ex'><code>{esc(short_gate_label(g.name))}</code>"
            f" <span class='fc-plan'>({esc(_plan_short_name(p))})</span></span>"
            for p, g in members_sorted
        )
        more = len(members) - len(members_sorted)
        if more > 0:
            examples_html += f" <span class='muted small'>+ {more} more</span>"
        rows.append(
            f"<tr>"
            f"<td class='fc-category'>{esc(cls_label)}</td>"
            f"<td class='num'>{len(members)}</td>"
            f"<td class='fc-examples'>{examples_html}</td>"
            f"</tr>"
        )

    plans_with_any = len({p.slug for p, _ in failing})

    # Build the takeaway dynamically from the actual top categories. If the
    # set of plans changes, this still names the dominant classes correctly.
    real_classes = [
        (label, members) for label, members in sorted_classes
        if members and label != "Other"
    ]
    top_names = [
        label.lower().replace(" / ", "/")
        for label, _ in real_classes[:3]
    ]
    if len(top_names) == 0:
        takeaway_html = ""
    else:
        if len(top_names) == 1:
            cluster_phrase = top_names[0]
        elif len(top_names) == 2:
            cluster_phrase = f"{top_names[0]} and {top_names[1]}"
        else:
            cluster_phrase = (
                ", ".join(top_names[:-1]) + f", and {top_names[-1]}"
            )
        takeaway_html = (
            f'<p class="muted small synthesis-takeaway">'
            f'<strong>Takeaway:</strong> '
            f'Most failures cluster around {esc(cluster_phrase)}. '
            f'These are the plan-generation areas to improve first.'
            f'</p>'
        )

    return f"""
<section class="slide">
  <header class="slide-head">
    <div class="kicker">cross-plan synthesis</div>
    <h1>Common failure classes</h1>
    <p class="lede">Every failing gate (DOOM or FRAGILE) across {plans_with_any} of {len(plans)} plans, grouped by failure type. Useful for spotting recurring weaknesses in the plans the generator produces &mdash; not just diagnosing them one at a time.</p>
  </header>
  {takeaway_html}
  <table class="failure-class-table">
    <thead>
      <tr><th>Failure class</th><th class='num'>Failing gates</th><th>Examples (worst first)</th></tr>
    </thead>
    <tbody>{''.join(rows)}</tbody>
  </table>
  <p class="muted small">{total_failing} failing gates total. Examples show short labels with the plan in parentheses; classification is by keyword on the full gate ID (first-match-wins). Some gates legitimately span categories; the priority order picks one.</p>
  <footer class="slide-foot"><span>Overview 5 / 9 &middot; common failure classes</span></footer>
</section>
"""


def _fixability_reason(plan: Plan) -> str:
    """Specific synthesis of *why* this plan's failure shape is narrow or wide.

    Describes the shape in concrete terms (counts of DOOM/FRAGILE/MARGINAL/
    ROBUST + supporting gates) rather than generic categories. The actual
    blocker gate name is shown in the adjacent "First fix" column, so this
    function deliberately omits the gate name to avoid duplication.
    """
    counts = {v: 0 for v in ("DOOM", "FRAGILE", "MARGINAL", "ROBUST")}
    for g in plan.gate_verdicts:
        if g.verdict in counts:
            counts[g.verdict] += 1
    d, f, m, r = counts["DOOM"], counts["FRAGILE"], counts["MARGINAL"], counts["ROBUST"]
    high_conf = sum(1 for g in plan.gate_verdicts if g.confidence_grade == "HIGH")
    low_conf = sum(1 for g in plan.gate_verdicts if g.confidence_grade == "LOW")
    n_unmod = len(plan.unmodelled_gate_names)
    pct = plan.worst_pass_rate * 100

    parts: list[str] = []

    # Shape description (the leading clause).
    if d == 0 and f == 0:
        parts.append("no failing gates")
    elif d == 0:
        parts.append(f"no DOOM gates; weakest at {pct:.0f}%")
    elif d == 1 and m + r > f:
        # Single hard blocker with supporting gates near or above threshold.
        supports = []
        if m:
            supports.append(f"{m} marginal")
        if r:
            supports.append(f"{r} robust")
        parts.append(
            "single hard blocker, " + " + ".join(supports)
            if supports
            else "single hard blocker"
        )
    elif d == 1:
        parts.append(f"1 DOOM + {f} FRAGILE")
    else:
        parts.append(f"{d} DOOM + {f} FRAGILE blockers")

    # Trust-calibration modifiers.
    if high_conf >= 2 and high_conf >= low_conf:
        parts.append("data-anchored")
    if n_unmod <= 2:
        parts.append("few unmodelled risks")

    return "; ".join(parts[:3])


def intro_slide_most_fixable(plans: list[Plan]) -> str:
    """Triage: rank plans by how close they are to viability."""
    indexed = list(enumerate(plans))

    def fix_key(ip: tuple[int, Plan]):
        _, p = ip
        n_doom = sum(1 for g in p.gate_verdicts if g.verdict == "DOOM")
        high_conf = sum(1 for g in p.gate_verdicts if g.confidence_grade == "HIGH")
        # Ascending sort = most-fixable first.
        return (
            n_doom,
            -p.worst_pass_rate,
            len(p.unmodelled_gate_names),
            -high_conf,
            p.slug,
        )

    sorted_indexed = sorted(indexed, key=fix_key)

    rows = []
    for orig_idx, p in sorted_indexed:
        band = BAND_LABEL.get(p.overall_band, p.overall_band.upper())
        color = BAND_COLOR.get(p.overall_band, "#666")
        pct = p.worst_pass_rate * 100
        shape, _, _ = classify_failure_shape(p)
        n_unmod = len(p.unmodelled_gate_names)
        reason = _fixability_reason(p)
        first_fix = short_gate_label(p.worst_gate) if p.worst_gate else "—"
        target_slide = INTRO_SLIDES + orig_idx * PER_PLAN
        rows.append(
            f"<tr class='roster-row' data-target='{target_slide}' "
            f"tabindex='0' role='link' "
            f"aria-label='Jump to {esc(p.name)}'>"
            f"<td class='plan-cell'>"
            f"<div class='plan-name'>{esc(p.name)}</div>"
            f"<code class='plan-slug'>{esc(p.slug)}</code>"
            f"</td>"
            f"<td><span class='band-pill' style='background:{color}'>{esc(band)}</span></td>"
            f"<td class='fix-shape'><code>{esc(shape)}</code></td>"
            f"<td class='num'>{pct:.1f}%</td>"
            f"<td class='num'>{n_unmod}</td>"
            f"<td class='fix-first'><code title='{esc(p.worst_gate)}'>{esc(first_fix)}</code></td>"
            f"<td class='fix-why'>{esc(reason)}</td>"
            f"</tr>"
        )

    return f"""
<section class="slide">
  <header class="slide-head">
    <div class="kicker">triage</div>
    <h1>Closest to viability</h1>
    <p class="lede">Plans ranked by fixability &mdash; least bad first. <strong>None of these plans currently pass</strong>; this is a relative ranking of where remediation effort would be cheapest. Sort: fewest DOOM gates &rarr; highest worst-gate pass rate &rarr; fewest unmodelled risks &rarr; highest data confidence.</p>
  </header>
  <table class="roster fix-table">
    <thead><tr>
      <th>Plan</th><th>Band</th><th>Failure shape</th>
      <th class='num'>Worst pass rate</th><th class='num'>Unmodelled</th>
      <th>First fix</th><th>Why fixable</th>
    </tr></thead>
    <tbody>{''.join(rows)}</tbody>
  </table>
  <footer class="slide-foot"><span>Overview 6 / 9 &middot; closest to viability</span></footer>
</section>
"""


def classify_failure_shape(plan: Plan) -> tuple[str, str, str]:
    """Return (shape_counts, label, interpretation) for a plan's gate verdicts.

    shape_counts: e.g. "1 DOOM + 4 MARGINAL"
    label: short tag like "Single blocker"
    interpretation: one-sentence reading
    """
    counts = {v: 0 for v in ("DOOM", "FRAGILE", "MARGINAL", "ROBUST")}
    for g in plan.gate_verdicts:
        if g.verdict in counts:
            counts[g.verdict] += 1
    f = counts["DOOM"] + counts["FRAGILE"]
    m = counts["MARGINAL"]
    r = counts["ROBUST"]
    u = len(plan.unmodelled_gate_names)

    parts = [f"{counts[v]} {v}" for v in ("DOOM", "FRAGILE", "MARGINAL", "ROBUST") if counts[v] > 0]
    shape = " + ".join(parts) if parts else "no declared gates"

    if f == 0 and (m + r) > 0:
        label = "Mostly robust"
        interp = "no failing gates under current bounds"
    elif f == 1 and (m + r) >= 1:
        label = "Single blocker"
        interp = "one primary blocker, otherwise on track"
    elif f >= 2 and f <= (m + r):
        label = "Multiple blockers"
        interp = "several failing gates, but more passing than not"
    elif f > 0 and f > (m + r):
        label = "Broadly weak"
        interp = "majority of declared gates fail under current bounds"
    else:
        label = "Mixed"
        interp = ""

    if u > 0 and u >= f + m + r:
        label = f"{label} &middot; unmodelled-heavy"
        extra = f"{u} out-of-model risks not simulated"
        interp = f"{interp} &middot; {extra}" if interp else extra

    return shape, label, interp


def _format_confidence_counts(plan: Plan) -> str:
    """Render per-gate confidence counts as e.g. '2 LOW · 3 MEDIUM · 0 HIGH'.
    Returns empty string if no confidence data is available."""
    counts = {"LOW": 0, "MEDIUM": 0, "HIGH": 0}
    unknown = 0
    for g in plan.gate_verdicts:
        grade = (g.confidence_grade or "").upper()
        if grade in counts:
            counts[grade] += 1
        else:
            unknown += 1
    # If no gate has any grade, show no data
    if sum(counts.values()) == 0 and unknown == len(plan.gate_verdicts):
        return ""
    parts = [
        f"<span class='conf-c conf-{grade.lower()}'>{counts[grade]} {grade}</span>"
        for grade in ("LOW", "MEDIUM", "HIGH")
    ]
    return " &middot; ".join(parts)


def slide_overview(plan: Plan) -> str:
    failed_n = len(plan.failed_gates)
    unmod_n = len(plan.unmodelled_gate_names)
    declared_n = len(plan.gate_verdicts)
    unmodelled_heavy = unmod_n > 0 and unmod_n >= declared_n
    badge = render_verdict_badge(
        plan.overall_band, plan.worst_gate, plan.worst_pass_rate,
        n_unmodelled=unmod_n, unmodelled_heavy=unmodelled_heavy,
    )
    shape, label, interp = classify_failure_shape(plan)
    conf_html = _format_confidence_counts(plan)
    confidence_block = (
        f"<div class='fs-block'>"
        f"<div class='fs-label'>Model confidence</div>"
        f"<div class='fs-confidence'>{conf_html}</div>"
        f"</div>"
        if conf_html else ""
    )
    return f"""
<section class="slide">
  <header class="slide-head">
    <div class="kicker">{esc(plan.slug)} &middot; {esc(plan.plan_type)}</div>
    <h1>{esc(plan.name)}</h1>
  </header>
  <div class="overview">
    <div class="goal">
      <h3>Goal</h3>
      <p>{esc(plan.primary_goal)}</p>
      <div class="metric-row">
        <div class="metric"><span class="metric-num">{failed_n}</span><span class="metric-cap">failed gates</span></div>
        <div class="metric"><span class="metric-num">{unmod_n}</span><span class="metric-cap">unmodelled existential gates</span></div>
        <div class="metric"><span class="metric-num">{len(plan.gate_verdicts)}</span><span class="metric-cap">declared gates</span></div>
      </div>
    </div>
    {badge}
  </div>
  <div class="failure-shape">
    <div class="fs-block">
      <div class="fs-label">Failure shape</div>
      <div class="fs-counts"><code>{esc(shape)}</code></div>
    </div>
    <div class="fs-block">
      <div class="fs-label">Fixability</div>
      <div class="fs-tag-row"><span class="fs-tag">{label}</span>
        <span class="fs-interp">{interp}</span>
      </div>
    </div>
    {confidence_block}
  </div>
  <footer class="slide-foot"><span>Slide 1 / 6 &middot; overview &amp; verdict</span></footer>
</section>
"""


def _basis_pill_class(basis: str) -> str:
    """Map threshold_basis values to a CSS class."""
    b = (basis or "").lower()
    if "explicit" in b:
        return "basis-explicit"
    if "inferred" in b:
        return "basis-inferred"
    if "derived" in b:
        return "basis-derived"
    if "model" in b or "assumption" in b:
        return "basis-model"
    return "basis-unknown"


def _format_scenario_value(v: float | None, condition: GateCondition | None) -> tuple[str, str]:
    """Return (display_str, css_class). Class flags fail/pass against the gate condition."""
    if v is None:
        return ("—", "")
    sign = "+" if v >= 0 else ""
    abs_v = abs(v)
    if abs_v >= 1_000_000_000:
        s = f"{sign}{v / 1_000_000_000:.2f}B"
    elif abs_v >= 1_000_000:
        s = f"{sign}{v / 1_000_000:.2f}M"
    elif abs_v >= 1_000:
        s = f"{sign}{v / 1_000:.2f}k"
    elif abs_v < 1:
        s = f"{sign}{v:.4f}"
    else:
        s = f"{sign}{v:.2f}"
    # Evaluate against condition: e.g. ">= 0" — fail if v < 0
    cls = ""
    if condition is not None:
        op, thr = condition.operator, condition.value
        passes = {
            ">=": v >= thr,
            ">": v > thr,
            "<=": v <= thr,
            "<": v < thr,
            "==": v == thr,
        }.get(op, None)
        if passes is True:
            cls = "sc-pass"
        elif passes is False:
            cls = "sc-fail"
    return (s, cls)


def slide_gate_chart(plan: Plan) -> str:
    chart = render_gate_bar_chart(plan.gate_verdicts)
    legend = """
    <div class="legend">
      <span><span class="sw" style="background:#c62828"></span>DOOM &lt;20%</span>
      <span><span class="sw" style="background:#ef6c00"></span>FRAGILE 20–50%</span>
      <span><span class="sw" style="background:#f9a825"></span>MARGINAL 50–80%</span>
      <span><span class="sw" style="background:#2e7d32"></span>ROBUST ≥80%</span>
    </div>
    """
    # Supplementary detail table: threshold condition, basis pill,
    # and low/base/high scenario outputs per gate.
    detail_rows = []
    for g in plan.gate_verdicts:
        cond = plan.gate_conditions.get(g.name)
        cond_str = (
            f"{cond.operator} {cond.value:g}" if cond else "—"
        )
        basis_cls = _basis_pill_class(g.threshold_basis)
        basis_label = (g.threshold_basis or "unknown").replace("_", " ")
        sc = plan.scenarios.get(g.name)
        if sc is None:
            low_disp, base_disp, high_disp = ("—", ""), ("—", ""), ("—", "")
            unit = ""
        else:
            low_disp = _format_scenario_value(sc.low, cond)
            base_disp = _format_scenario_value(sc.base, cond)
            high_disp = _format_scenario_value(sc.high, cond)
            unit = sc.unit
        unit_cell = f"<span class='muted small'>{esc(unit)}</span>" if unit else ""
        detail_rows.append(
            f"<tr>"
            f"<td><code>{esc(g.name)}</code></td>"
            f"<td class='cond'>{esc(cond_str)}</td>"
            f"<td><span class='basis-pill {basis_cls}'>{esc(basis_label)}</span></td>"
            f"<td class='num scen {low_disp[1]}'>{esc(low_disp[0])}</td>"
            f"<td class='num scen {base_disp[1]}'>{esc(base_disp[0])}</td>"
            f"<td class='num scen {high_disp[1]}'>{esc(high_disp[0])}</td>"
            f"<td>{unit_cell}</td>"
            f"</tr>"
        )
    detail_table = f"""
    <table class="gate-detail">
      <thead>
        <tr>
          <th>Gate</th>
          <th>Condition</th>
          <th>Threshold basis</th>
          <th class='num'>Low</th>
          <th class='num'>Base</th>
          <th class='num'>High</th>
          <th>Unit</th>
        </tr>
      </thead>
      <tbody>{''.join(detail_rows)}</tbody>
    </table>
    <p class="muted small">Scenario columns show each output at the <em>low</em>, <em>base</em>, and <em>high</em> deterministic input scenarios. Green = the gate passes its condition; red = the gate fails. The <strong>base</strong> column is the most telling: red there means the plan already fails under its own central assumptions, not just in tail cases.</p>
    """
    return f"""
<section class="slide">
  <header class="slide-head">
    <div class="kicker">{esc(plan.slug)} &middot; {esc(plan.plan_type)}</div>
    <h1>Gate pass rates</h1>
  </header>
  <div class="chart-wrap">
    {chart}
  </div>
  {legend}
  {detail_table}
  <footer class="slide-foot"><span>Slide 2 / 6 &middot; gate pass rates</span></footer>
</section>
"""


def slide_failure_drivers(plan: Plan) -> str:
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

    return f"""
<section class="slide">
  <header class="slide-head">
    <div class="kicker">{esc(plan.slug)} &middot; {esc(plan.plan_type)}</div>
    <h1>Failure drivers</h1>
  </header>
  <div class="panel">
    {drv_table}
  </div>
  <footer class="slide-foot"><span>Slide 3 / 6 &middot; failure drivers (modelled)</span></footer>
</section>
"""


def slide_missing_inputs(plan: Plan) -> str:
    if plan.missing_inputs:
        rows = []
        for mi in plan.missing_inputs:
            source = mi.source or "unknown"
            # "assumption" → louder, since these are pure model guesses;
            # "data" → quieter, anchored in the report's narrative.
            cls = "src-assumption" if "assumption" in source.lower() else "src-data"
            label = source.replace("_", " ")
            rows.append(
                f"<tr>"
                f"<td class='num'>{mi.rank}</td>"
                f"<td><code>{esc(mi.input_id)}</code></td>"
                f"<td><code>{esc(mi.worst_gate)}</code></td>"
                f"<td class='num'>{mi.score:.1f}</td>"
                f"<td class='num'>{mi.bound_width_ratio:.2f}</td>"
                f"<td><span class='basis-pill {cls}'>{esc(label)}</span></td>"
                f"</tr>"
            )
        body = f"""
        <table class="data-table">
          <thead><tr>
            <th>Rank</th>
            <th>Missing input</th>
            <th>Worst-affected gate</th>
            <th class='num'>Score</th>
            <th class='num'>Bound width &divide; base</th>
            <th>Basis</th>
          </tr></thead>
          <tbody>{''.join(rows)}</tbody>
        </table>
        <p class="muted small">Higher score = more decision value from pinning down this input. <strong>Assumption</strong> bounds have no narrative anchor; <strong>data</strong> bounds are anchored in the source report (but still not empirical ground truth).</p>
        """
    else:
        body = '<p class="muted">No missing inputs ranked for this plan.</p>'
    return f"""
<section class="slide">
  <header class="slide-head">
    <div class="kicker">{esc(plan.slug)} &middot; {esc(plan.plan_type)}</div>
    <h1>What to measure next</h1>
    <p class="lede">Missing inputs ranked by their impact on the simulation. Replacing a high-scoring assumption with a measured value is the cheapest win for the model's predictive value.</p>
  </header>
  <div class="panel">
    {body}
  </div>
  <footer class="slide-foot"><span>Slide 4 / 6 &middot; what to measure next</span></footer>
</section>
"""


def _truncate(text: str, limit: int) -> str:
    text = text or ""
    return text if len(text) <= limit else (text[:limit].rstrip() + "…")


def slide_unmodelled_gates(plan: Plan) -> str:
    if plan.unmodelled_gates:
        cards = []
        for g in plan.unmodelled_gates:
            why_html = (
                f"<div class='um-section'>"
                f"<div class='um-label'>Why it matters</div>"
                f"<div class='um-text'>{esc(_truncate(g.why, 320))}</div>"
                f"</div>" if g.why else ""
            )
            cons_html = (
                f"<div class='um-section'>"
                f"<div class='um-label um-label-cons'>If false</div>"
                f"<div class='um-text'>{esc(_truncate(g.consequence, 320))}</div>"
                f"</div>" if g.consequence else ""
            )
            source_html = (
                f"<div class='um-source'>source: {esc(g.source_anchor)}</div>"
                if g.source_anchor else ""
            )
            cards.append(
                f"<li class='um-card'>"
                f"<div class='um-gate'><code>{esc(g.name)}</code>{source_html}</div>"
                f"{why_html}"
                f"{cons_html}"
                f"</li>"
            )
        um_block = f"<ul class='um-list'>{''.join(cards)}</ul>"
    else:
        um_block = '<p class="muted">No unmodelled existential gates flagged.</p>'

    return f"""
<section class="slide">
  <header class="slide-head">
    <div class="kicker">{esc(plan.slug)} &middot; {esc(plan.plan_type)}</div>
    <h1>Unmodelled existential gates</h1>
  </header>
  <div class="panel">
    <p class="muted small">The simulation does not test these. Treat all modelled pass rates as conditional on them holding.</p>
    {um_block}
  </div>
  <footer class="slide-foot"><span>Slide 5 / 6 &middot; unmodelled existential gates</span></footer>
</section>
"""


def slide_what_to_change_next(plan: Plan) -> str:
    """Synthesizing slide: prescriptive actions derived from failing gates +
    failure drivers + unmodelled gates."""
    # Failing modelled gates, worst-first
    failing = sorted(
        (g for g in plan.gate_verdicts if g.verdict in ("DOOM", "FRAGILE")),
        key=lambda g: g.pass_rate,
    )
    drivers_by_gate = {d.gate: d for d in plan.failure_drivers}

    items: list[str] = []
    for g in failing:
        drv = drivers_by_gate.get(g.name)
        is_worst = g.name == plan.worst_gate
        tag_label = "WORST GATE" if is_worst else g.verdict
        tag_cls = "tag-worst" if is_worst else f"tag-{g.verdict.lower()}"
        if drv and drv.top_driver and "saturated" not in drv.top_driver.lower():
            req = drv.pass_requires or f"move {drv.top_driver} into the passing range"
            action = (
                f"Bring <code>{esc(drv.top_driver)}</code> into the passing range "
                f"&mdash; {esc(req)}."
            )
        elif drv and "saturated" in (drv.top_driver or "").lower():
            action = (
                "Re-examine the input bounds and threshold &mdash; "
                "no single input restriction can lift the pass rate from current bounds."
            )
        else:
            action = (
                f"Investigate failure paths for <code>{esc(g.name)}</code> "
                f"(verdict {g.verdict})."
            )
        items.append(
            f"<li><div class='action-head'>"
            f"<code>{esc(g.name)}</code> "
            f"<span class='action-tag {tag_cls}'>{tag_label}</span>"
            f"</div><div class='action-do'>{action}</div></li>"
        )

    # Out-of-model risks: convert unmodelled gates into acceptance criteria
    for um in plan.unmodelled_gates[:3]:
        items.append(
            f"<li><div class='action-head'>"
            f"<code>{esc(um.name)}</code> "
            f"<span class='action-tag tag-unmod'>UNMODELLED</span>"
            f"</div><div class='action-do'>Convert this assumption into an explicit "
            f"acceptance criterion before the next commit point.</div></li>"
        )

    if not items:
        body = '<p class="muted">No actionable blockers identified for this plan.</p>'
    else:
        body = f'<ol class="action-list">{"".join(items)}</ol>'

    return f"""
<section class="slide">
  <header class="slide-head">
    <div class="kicker">{esc(plan.slug)} &middot; {esc(plan.plan_type)}</div>
    <h1>What to change next</h1>
    <p class="lede">Prescriptive synthesis &mdash; one action per blocker, derived from the failure drivers and the out-of-model risks. Modelled blockers come first (worst gate at the top), then unmodelled gates to lock down.</p>
  </header>
  <div class="panel">
    {body}
  </div>
  <footer class="slide-foot"><span>Slide 6 / 6 &middot; what to change next</span></footer>
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
  position: relative;
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
.slide-head { border-bottom: 1px solid var(--rule); padding-bottom: 16px; margin-bottom: 22px; padding-right: 160px; }
.slide-head .kicker {
  font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--kicker); font-family: ui-monospace, "SF Mono", Menlo, monospace;
}
.slide-head h1 { font-size: 28px; margin: 6px 0 0; font-weight: 600; line-height: 1.25; }
.snapshot-link {
  position: absolute; top: 38px; right: 48px;
  font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--kicker); font-family: ui-monospace, "SF Mono", Menlo, monospace;
  text-decoration: none; padding: 4px 6px; margin: -4px -6px;
  border-radius: 3px;
}
.snapshot-link:hover { color: var(--ink); background: rgba(0,0,0,0.04); }
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
.verdict-caveat {
  margin-top: 16px; padding-top: 12px;
  border-top: 1px solid rgba(255,255,255,0.30);
  font-size: 11px; line-height: 1.55;
  color: rgba(255,255,255,0.92);
}
.verdict-caveat-headline {
  font-weight: 700; letter-spacing: 0.02em;
  margin-bottom: 4px;
}

/* Failure shape / fixability card on plan overview slide */
.failure-shape {
  margin-top: 22px; padding: 14px 18px;
  background: #fafaf8; border-left: 3px solid var(--ink);
  border-radius: 0 4px 4px 0;
  display: grid; grid-template-columns: auto 1fr auto; gap: 28px;
  align-items: start;
}
.fs-block { min-width: 0; }
.fs-label {
  font-size: 10px; letter-spacing: 0.1em; text-transform: uppercase;
  color: var(--muted); font-weight: 600; margin-bottom: 6px;
}
.fs-counts { font-size: 14px; }
.fs-counts code { font-family: ui-monospace, monospace; font-size: 13px; }
.fs-tag-row { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }
.fs-tag {
  background: var(--ink); color: white;
  padding: 4px 12px; border-radius: 12px;
  font-size: 11px; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase;
}
.fs-interp { color: var(--muted); font-size: 13px; }
.fs-confidence { font-size: 13px; font-family: ui-monospace, monospace; white-space: nowrap; }
.conf-c { font-weight: 600; }
.conf-c.conf-low { color: #b3300f; }
.conf-c.conf-medium { color: #8a6d0a; }
.conf-c.conf-high { color: #1e6d2c; }

/* Chart slide */
.chart-wrap { padding: 8px 0; }
.legend { display: flex; flex-wrap: wrap; justify-content: center; gap: 18px; font-size: 12px; color: var(--muted); margin-top: 8px; }
.legend .sw { display: inline-block; width: 12px; height: 12px; border-radius: 2px; vertical-align: middle; margin-right: 6px; }

/* Intro slides */
.title-slide .slide-head h1 { font-size: 42px; letter-spacing: -0.01em; }
.title-slide .slide-head .lede { font-size: 15px; max-width: 80ch; }
.dist-strip {
  display: flex; height: 150px; margin: 32px 0 28px;
  border-radius: 6px; overflow: hidden;
  box-shadow: 0 2px 12px rgba(0,0,0,0.10);
}
.strip-seg {
  color: white; padding: 18px 24px; min-width: 0;
  display: flex; flex-direction: column; justify-content: space-between;
}
.strip-label {
  font-size: 12px; letter-spacing: 0.14em; font-weight: 600; opacity: 0.92;
}
.strip-count {
  font-size: 52px; font-weight: 700; line-height: 1;
  display: flex; align-items: baseline; gap: 12px;
}
.strip-pct { font-size: 18px; font-weight: 500; opacity: 0.85; }
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
.chart-wrap.big { padding: 8px 0 8px; }
.roster { width: 100%; border-collapse: collapse; font-size: 13px; margin-top: 8px; }
.roster th, .roster td {
  padding: 9px 10px; border-bottom: 1px solid var(--rule);
  text-align: left; vertical-align: middle;
}
.roster th {
  font-size: 10px; text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--muted); font-weight: 600;
}
.roster tbody tr.roster-row { cursor: pointer; transition: background-color 0.12s; }
.roster tbody tr.roster-row:hover { background: #f1f1ef; }
.roster tbody tr.roster-row:focus { outline: 2px solid #1c1c1c; outline-offset: -2px; background: #f1f1ef; }
.roster tbody tr.roster-row:hover .plan-name { text-decoration: underline; }
.roster td.plan-cell { line-height: 1.3; }
.roster .plan-name { font-weight: 500; font-size: 13px; color: var(--ink); }
.roster .plan-slug { font-size: 10.5px; color: var(--muted); display: block; margin-top: 2px; }
.roster th.num, .roster td.num { text-align: right; font-variant-numeric: tabular-nums; }
.roster td.num { font-weight: 600; }
.roster td.warn-num { color: #b3300f; }
.roster td.bar-cell { width: 220px; }
.roster .wg { font-size: 11px; }
.band-pill {
  display: inline-block; padding: 3px 10px; border-radius: 12px;
  color: white; font-size: 10px; font-weight: 700; letter-spacing: 0.06em;
}
.mini-bar { width: 100%; height: 10px; background: var(--rule); border-radius: 5px; overflow: hidden; }
.mini-bar-fill { height: 100%; }
.roster td.base-cell { white-space: nowrap; }
.pass-fail {
  display: inline-block; padding: 2px 7px; border-radius: 4px;
  font-size: 10px; font-weight: 700; letter-spacing: 0.06em;
}
.pass-fail.pf-pass { background: #e8f4ea; color: #1e6d2c; }
.pass-fail.pf-fail { background: #fdecec; color: #b3300f; }
.pass-fail.pf-unknown { background: #f0f0ee; color: #555; }
.base-val {
  margin-left: 8px; font-weight: 600;
  font-variant-numeric: tabular-nums; font-size: 12px;
}
.base-unit { margin-left: 6px; color: var(--muted); font-size: 11px; }
.roster-footnote { margin-top: 12px; }
.vdist-cell { width: 280px; }
.vdist-bar {
  display: flex; height: 26px; width: 100%;
  border-radius: 4px; overflow: hidden;
  border: 1px solid var(--rule);
}
.vdist-bar.empty { background: var(--rule); }
.vdist-seg {
  display: flex; align-items: center; justify-content: center;
  color: white; font-size: 11px; font-weight: 600;
  min-width: 0; padding: 0 2px;
}

/* Methodology slides */
.methodology-body { max-width: 78ch; font-size: 14px; line-height: 1.6; color: var(--ink); }
.methodology-body h3 {
  font-size: 12px; text-transform: uppercase; letter-spacing: 0.1em;
  color: var(--muted); margin: 22px 0 10px; font-weight: 600;
}
.methodology-body p { margin: 0 0 14px; }
.methodology-body ul { padding-left: 22px; margin: 0 0 14px; }
.methodology-body li { margin-bottom: 8px; }
.methodology-body ul ul { margin: 8px 0 0; padding-left: 22px; }
.methodology-body code {
  font-size: 0.88em; padding: 1px 5px; background: #f0f0ec;
  border-radius: 3px; color: var(--ink);
}
.methodology-body em { color: var(--muted); }
.methodology-body p > em:only-child {
  display: block; padding: 12px 16px; background: #fafaf8;
  border-left: 3px solid var(--rule); border-radius: 0 4px 4px 0;
  color: var(--muted); font-size: 13px; font-style: italic; margin-top: 6px;
}

/* Common failure classes slide */
.failure-class-table {
  width: 100%; border-collapse: collapse; font-size: 13px; margin: 4px 0 12px;
}
.failure-class-table th, .failure-class-table td {
  padding: 12px 14px; border-bottom: 1px solid var(--rule);
  text-align: left; vertical-align: top;
}
.failure-class-table th {
  font-size: 10px; text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--muted); font-weight: 600;
}
.failure-class-table th.num, .failure-class-table td.num {
  text-align: right; font-variant-numeric: tabular-nums;
}
.failure-class-table td.num { font-weight: 700; font-size: 20px; width: 70px; }
.failure-class-table td.fc-category { font-weight: 600; font-size: 14px; width: 220px; }
.failure-class-table td.fc-examples { color: var(--muted); font-size: 12px; line-height: 1.7; }
.failure-class-table td.fc-examples code { color: var(--ink); font-size: 11.5px; }
.fc-plan { color: var(--muted); }
.fc-ex { white-space: nowrap; }
.synthesis-takeaway {
  margin: 6px 0 16px; padding: 10px 14px;
  background: #fafaf8; border-left: 3px solid var(--ink);
  border-radius: 0 4px 4px 0; line-height: 1.55;
}
.synthesis-takeaway strong { color: var(--ink); }

/* Most-fixable triage table */
.fix-table td.fix-shape code { font-size: 11px; }
.fix-table td.fix-first code {
  font-size: 11.5px; font-weight: 600;
  background: #fff7f0; color: #b3300f; padding: 2px 6px; border-radius: 3px;
}
.fix-table td.fix-why { font-size: 12px; color: var(--ink); line-height: 1.5; max-width: 280px; }

/* Base-case finding slide */
.bc-headline {
  display: flex; align-items: center; gap: 28px;
  margin: 24px 0; padding: 26px 28px;
  background: #fdecec; border-left: 5px solid #c62828; border-radius: 0 6px 6px 0;
}
.bc-num {
  font-size: 64px; font-weight: 800; line-height: 1;
  color: #c62828; letter-spacing: -0.02em;
  font-variant-numeric: tabular-nums; white-space: nowrap;
}
.bc-text { font-size: 15px; line-height: 1.55; max-width: 55ch; }
.bc-text strong { font-size: 16px; }
.bc-section-title {
  margin: 22px 0 10px; font-size: 11px; text-transform: uppercase;
  letter-spacing: 0.1em; color: var(--muted); font-weight: 600;
}
.bc-examples td.bc-val { color: #b3300f; font-weight: 700; }
.bc-examples td.bc-class { font-weight: 600; font-size: 12px; width: 180px; }

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
.data-table th.num, .data-table td.num { text-align: right; font-variant-numeric: tabular-nums; }
.basis-pill {
  display: inline-block; padding: 2px 8px; border-radius: 10px;
  font-size: 10px; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase;
  border: 1px solid transparent;
}
.basis-pill.src-assumption { background: #fff7f0; color: #b3300f; border-color: #ef6c00; }
.basis-pill.src-data { background: #f1f4ef; color: #1e6d2c; border-color: #c8d4c0; }
.basis-pill.basis-explicit { background: #eef2ee; color: #1e4d2c; border-color: #b8c7b3; }
.basis-pill.basis-inferred { background: #f0f0f4; color: #3a3a78; border-color: #b9b9d0; }
.basis-pill.basis-derived  { background: #f4f0eb; color: #6b4a23; border-color: #d3c1a8; }
.basis-pill.basis-model    { background: #fff7f0; color: #b3300f; border-color: #ef6c00; }
.basis-pill.basis-unknown  { background: #f3f3f1; color: #555; border-color: #d8d8d4; }

/* Gate detail table on slide 2 */
.gate-detail {
  width: 100%; border-collapse: collapse; font-size: 12px; margin-top: 16px;
}
.gate-detail th, .gate-detail td {
  padding: 6px 10px; border-bottom: 1px solid var(--rule); vertical-align: middle;
}
.gate-detail th {
  font-size: 10px; text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--muted); font-weight: 600; text-align: left;
}
.gate-detail th.num, .gate-detail td.num {
  text-align: right; font-variant-numeric: tabular-nums;
}
.gate-detail td.cond { font-family: ui-monospace, monospace; font-size: 11px; color: var(--muted); }
.gate-detail td.scen { font-weight: 600; }
.gate-detail td.scen.sc-pass { color: #1e6d2c; }
.gate-detail td.scen.sc-fail { color: #b3300f; }
.um-list { list-style: none; padding: 0; margin: 8px 0 0; }
.um-card {
  padding: 14px 0; border-bottom: 1px solid var(--rule);
}
.um-card:last-child { border-bottom: none; padding-bottom: 4px; }
.um-gate {
  font-size: 14px; margin-bottom: 10px;
  display: flex; align-items: baseline; gap: 12px; flex-wrap: wrap;
}
.um-source {
  font-size: 10px; letter-spacing: 0.06em; text-transform: uppercase;
  color: var(--muted); font-family: ui-monospace, monospace;
}
.um-section { margin-bottom: 8px; }
.um-section:last-child { margin-bottom: 0; }
.um-label {
  font-size: 10px; text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--muted); font-weight: 600; margin-bottom: 3px;
}
.um-label.um-label-cons { color: #b3300f; }
.um-text { font-size: 13px; line-height: 1.5; color: var(--ink); }

/* What to change next */
.action-list { padding-left: 28px; margin: 0; }
.action-list li { margin-bottom: 18px; line-height: 1.5; }
.action-head { font-size: 13px; margin-bottom: 5px; display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }
.action-head code { font-size: 12px; }
.action-do { font-size: 14px; }
.action-do code { font-family: ui-monospace, monospace; font-size: 0.92em; }
.action-tag {
  display: inline-block; padding: 2px 8px; border-radius: 10px;
  font-size: 10px; font-weight: 700; letter-spacing: 0.06em;
}
.action-tag.tag-worst { background: #c62828; color: white; }
.action-tag.tag-doom { background: #fdecec; color: #b3300f; border: 1px solid #c62828; }
.action-tag.tag-fragile { background: #fdf1e7; color: #8a3d0a; border: 1px solid #ef6c00; }
.action-tag.tag-unmod { background: #f0f0ee; color: #555; border: 1px solid #b8b8b4; }
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

JS_TEMPLATE = r"""
// Move the snapshot link inside each slide so it scrolls with the slide content
// rather than being pinned to the viewport.
{
  const link = document.querySelector('.snapshot-link');
  if (link) {
    document.querySelectorAll('.slide').forEach((s) => s.appendChild(link.cloneNode(true)));
    link.remove();
  }
}
const INTRO_SLIDES = __INTRO_SLIDES__;
const PER_PLAN = __PER_PLAN__;
const slides = Array.from(document.querySelectorAll('.slide'));
const counter = document.getElementById('counter');
const progress = document.getElementById('progress-bar');
const select = document.getElementById('plan-select');
let idx = 0;
// pushHistory=true adds a new history entry (used for explicit jumps so the
// browser back button returns to the previous slide). Continuous navigation
// (arrow keys, prev/next buttons) uses replaceState to avoid polluting history.
function show(i, pushHistory) {
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
  const hash = '#s' + (idx + 1);
  const state = { idx };
  if (pushHistory && location.hash !== hash) {
    history.pushState(state, '', hash);
  } else {
    history.replaceState(state, '', hash);
  }
}
document.getElementById('prev').addEventListener('click', () => show(idx - 1, false));
document.getElementById('next').addEventListener('click', () => show(idx + 1, false));
select.addEventListener('change', (e) => {
  const si = e.target.selectedIndex;
  show(si === 0 ? 0 : INTRO_SLIDES + (si - 1) * PER_PLAN, true);
});
document.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') { e.preventDefault(); show(idx + 1, false); }
  else if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); show(idx - 1, false); }
  else if (e.key === 'Home') { e.preventDefault(); show(0, false); }
  else if (e.key === 'End') { e.preventDefault(); show(slides.length - 1, false); }
});
// roster row click-to-jump (explicit nav → push history)
document.querySelectorAll('tr.roster-row').forEach((row) => {
  const target = parseInt(row.dataset.target, 10);
  if (!Number.isFinite(target)) return;
  row.addEventListener('click', () => show(target, true));
  row.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); show(target, true); }
  });
});
// browser back/forward — restore slide from state (or fall back to hash)
window.addEventListener('popstate', (e) => {
  let target;
  if (e.state && Number.isFinite(e.state.idx)) {
    target = e.state.idx;
  } else {
    const m = (location.hash || '').match(/^#s(\d+)$/);
    target = m ? parseInt(m[1], 10) - 1 : 0;
  }
  show(target, false);
});
// initial load — hash-based deep link
const initial = (location.hash || '').match(/^#s(\d+)$/);
show(initial ? parseInt(initial[1], 10) - 1 : 0, false);
"""


def render_html(plans: list[Plan]) -> str:
    stats = compute_stats(plans)
    methodology = extract_slides(METHODOLOGY_PATH) if METHODOLOGY_PATH.exists() else []
    # Findings → triage first; methodology + reference views at the end.
    methodology_html = [
        slide_methodology(m, 7 + i, INTRO_SLIDES)
        for i, m in enumerate(methodology[:2])  # only Slide A & Slide B
    ]
    slides_html = [
        intro_slide_headline(stats),               # 1/9 — Headline figures
        intro_slide_distribution(stats),           # 2/9 — Verdict distribution
        intro_slide_roster(plans),                 # 3/9 — Plan roster
        intro_slide_base_case_failure(plans),      # 4/9 — Base-case finding
        intro_slide_failure_clustering(plans),     # 5/9 — Common failure classes
        intro_slide_most_fixable(plans),           # 6/9 — Most-fixable triage
        *methodology_html,                         # 7/9, 8/9 — Methodology A, B
        intro_slide_histogram(plans),              # 9/9 — Gate verdicts by plan
    ]
    options = ['<option value="overview">— Overview —</option>']
    for i, plan in enumerate(plans):
        slides_html.append(slide_overview(plan))
        slides_html.append(slide_gate_chart(plan))
        slides_html.append(slide_failure_drivers(plan))
        slides_html.append(slide_missing_inputs(plan))
        slides_html.append(slide_unmodelled_gates(plan))
        slides_html.append(slide_what_to_change_next(plan))
        band_label = BAND_LABEL.get(plan.overall_band, plan.overall_band.upper())
        options.append(
            f'<option value="{i}">{esc(plan.slug)} — {esc(plan.name)} [{esc(band_label)}]</option>'
        )

    total_slides = INTRO_SLIDES + len(plans) * PER_PLAN
    js = (JS_TEMPLATE
          .replace("__INTRO_SLIDES__", str(INTRO_SLIDES))
          .replace("__PER_PLAN__", str(PER_PLAN)))
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>PlanExe snapshot 46 — assessment slideshow</title>
<style>{CSS}</style>
</head>
<body>
<a class="snapshot-link"
   href="https://github.com/PlanExeOrg/PlanExe-results-napkin-math/tree/main/snapshot/46"
   target="_blank" rel="noopener">Snapshot 46</a>
<div class="deck">
{''.join(slides_html)}
</div>
<div class="nav">
  <button id="prev" aria-label="Previous slide">← Prev</button>
  <button id="next" aria-label="Next slide">Next →</button>
  <select id="plan-select" aria-label="Jump to plan">
    {''.join(options)}
  </select>
  <span class="counter" id="counter">1 / {total_slides}</span>
  <div class="progress"><div id="progress-bar" style="width:0%"></div></div>
</div>
<script>{js}</script>
</body>
</html>
"""


def validate_plans(plans: list[Plan]) -> list[str]:
    """Check parsed plans for silent-regression smells. Returns a list of
    human-readable problem strings; empty list means OK."""
    problems: list[str] = []
    for p in plans:
        # Plan name should not fall back to the slug.
        if p.name == p.slug:
            problems.append(
                f"{p.slug}: plan_name fell back to slug — JSON block may be unreadable"
            )
        # Verdict band must be one of the known values.
        if p.overall_band not in ("doom", "fragile", "marginal", "viable", "unknown"):
            problems.append(f"{p.slug}: unexpected overall_band={p.overall_band!r}")
        # Confidence counts (when present) should sum to declared gate count.
        graded = sum(
            1 for g in p.gate_verdicts
            if (g.confidence_grade or "").upper() in ("LOW", "MEDIUM", "HIGH")
        )
        if graded > 0 and graded != len(p.gate_verdicts):
            problems.append(
                f"{p.slug}: confidence grades cover {graded}/{len(p.gate_verdicts)} "
                "declared gates"
            )
    return problems


def main() -> None:
    plan_dirs = sorted(
        d for d in SNAPSHOT_DIR.iterdir()
        if d.is_dir() and (d / "assessment.md").exists()
    )
    plans = [parse_assessment(d.name, d / "assessment.md") for d in plan_dirs]
    problems = validate_plans(plans)
    if problems:
        print("VALIDATION PROBLEMS:")
        for p in problems:
            print(f"  - {p}")
        raise SystemExit(
            f"Refusing to write slideshow: {len(problems)} validation problem(s). "
            "Fix the parser or run with relaxed validation."
        )
    OUTPUT_PATH.write_text(render_html(plans), encoding="utf-8")
    total = INTRO_SLIDES + len(plans) * PER_PLAN
    stats = compute_stats(plans)
    print(f"Wrote {OUTPUT_PATH}: {INTRO_SLIDES} overview + "
          f"{len(plans)} plans × {PER_PLAN} = {total} slides.")
    print(
        f"Validation passed: {stats.total_plans} plans · "
        f"{stats.total_declared_gates} declared gates · "
        f"{stats.total_failed_gates} failed · "
        f"{stats.total_unmodelled} unmodelled"
    )


if __name__ == "__main__":
    main()
