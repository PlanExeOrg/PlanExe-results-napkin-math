"""Extract `### Slide A — ...` / `### Slide B — ...` sections from methology.md
and render each section's body to HTML for embedding in the slideshow.

The Markdown subset handled covers exactly what methology.md uses:
- Bullet lists (with one level of `  -` nesting)
- Bold (`**...**`) and italics (`*...*`) inline
- Inline code (`` ` ... ` ``)
- Bold-only single-line paragraphs ending in `:` treated as sub-headings
- Italic-only paragraphs (kept as `<em>` paragraphs, so the slide CSS can give
  the trailing caption an aside-style treatment)
"""

from __future__ import annotations

import html
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass
class MethodologySlide:
    key: str       # e.g. "A", "B"
    title: str     # e.g. "How the simulation works"
    body_html: str  # rendered HTML, ready to embed inside the slide template


def extract_slides(md_path: Path) -> list[MethodologySlide]:
    """Return one MethodologySlide per `### Slide <K> — <Title>` heading,
    in document order. Body extends up to the next `### ` heading or EOF."""
    text = md_path.read_text(encoding="utf-8")
    pattern = re.compile(
        r"^### Slide ([A-Z]) — (.+?)\n(.*?)(?=^### |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    slides: list[MethodologySlide] = []
    for m in pattern.finditer(text):
        slides.append(MethodologySlide(
            key=m.group(1),
            title=m.group(2).strip(),
            body_html=md_to_html(m.group(3).strip()),
        ))
    return slides


# ---- Markdown -> HTML (minimal, scoped to methology.md's subset) ----

def md_to_html(md: str) -> str:
    md = md.strip()
    if not md:
        return ""
    out: list[str] = []
    for block in re.split(r"\n\s*\n", md):
        block = block.strip()
        if not block:
            continue
        if _is_bullet_list(block):
            out.append(_render_list(block))
        elif (sub_match := re.fullmatch(r"\*\*([^*]+)\*\*", block)) and _is_sub_heading(block):
            inner = sub_match.group(1).rstrip(":")
            out.append(f"<h3>{_inline(inner)}</h3>")
        else:
            text = " ".join(ln.strip() for ln in block.split("\n"))
            out.append(f"<p>{_inline(text)}</p>")
    return "\n".join(out)


def _is_bullet_list(block: str) -> bool:
    return bool(re.match(r"\s*-\s", block.split("\n", 1)[0]))


def _is_sub_heading(block: str) -> bool:
    s = block.strip()
    if "\n" in s:
        return False
    m = re.fullmatch(r"\*\*([^*]+)\*\*", s)
    return bool(m and m.group(1).rstrip().endswith(":"))


def _render_list(block: str) -> str:
    """Parse a bullet block (one level of nesting) into nested <ul><li>."""
    items: list[dict] = []
    current: dict | None = None
    for ln in block.split("\n"):
        m = re.match(r"(\s*)-\s+(.+)", ln)
        if m:
            if current is not None:
                items.append(current)
            current = {"indent": len(m.group(1)), "text": m.group(2)}
        elif ln.strip() and current is not None:
            current["text"] += " " + ln.strip()
    if current is not None:
        items.append(current)

    parts = ["<ul>"]
    i = 0
    while i < len(items):
        top = items[i]
        if top["indent"] > 0:
            i += 1
            continue
        parts.append(f"<li>{_inline(top['text'])}")
        j = i + 1
        nested: list[dict] = []
        while j < len(items) and items[j]["indent"] > 0:
            nested.append(items[j])
            j += 1
        if nested:
            parts.append("<ul>")
            for n in nested:
                parts.append(f"<li>{_inline(n['text'])}</li>")
            parts.append("</ul>")
        parts.append("</li>")
        i = j
    parts.append("</ul>")
    return "".join(parts)


_PLACEHOLDER = "\x00MD{0}\x00"


def _inline(s: str) -> str:
    """Render inline markup. Order matters: pull code and bold out into
    placeholders before processing italics, so single-asterisk italic runs
    can't be tripped up by bold/code content."""
    # 1. Inline code -> placeholder (content is literal, escape later)
    codes: list[str] = []
    def code_sub(m: re.Match) -> str:
        codes.append(m.group(1))
        return _PLACEHOLDER.format("C" + str(len(codes) - 1))
    s = re.sub(r"`([^`]+)`", code_sub, s)

    # 2. Bold -> placeholder
    bolds: list[str] = []
    def bold_sub(m: re.Match) -> str:
        bolds.append(m.group(1))
        return _PLACEHOLDER.format("B" + str(len(bolds) - 1))
    s = re.sub(r"\*\*([^*]+?)\*\*", bold_sub, s)

    # 3. Italics (safe now that bold markers are gone)
    s = re.sub(r"\*([^*]+?)\*", r"<em>\1</em>", s)

    # 4. Restore bold (allow italics inside the bold span)
    for i, b in enumerate(bolds):
        b_html = re.sub(r"\*([^*]+?)\*", r"<em>\1</em>", b)
        s = s.replace(_PLACEHOLDER.format("B" + str(i)), f"<strong>{b_html}</strong>")

    # 5. Restore code (escape its contents)
    for i, c in enumerate(codes):
        s = s.replace(
            _PLACEHOLDER.format("C" + str(i)),
            f"<code>{html.escape(c, quote=True)}</code>",
        )
    return s


if __name__ == "__main__":
    # Smoke test
    here = Path(__file__).parent / "snapshot" / "46" / "methology.md"
    for sl in extract_slides(here):
        print(f"=== Slide {sl.key}: {sl.title} ===")
        print(sl.body_html[:300] + ("..." if len(sl.body_html) > 300 else ""))
        print()
