#!/usr/bin/env python3
"""Polish the shared-case teaser without changing either search-tree geometry.

Keep branch paths, node centers, solid/dashed semantics and photographic crops.
Tighten the case/header spacing and use flat, aligned graphic groups.
The script is idempotent and overwrites the stable source, not a new candidate.
"""
from copy import deepcopy
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "figures/candidates/teaser-v6-paper-wording/teaser.svg"
SVG = "http://www.w3.org/2000/svg"
XLINK = "http://www.w3.org/1999/xlink"
INK = "http://www.inkscape.org/namespaces/inkscape"
NS = {"s": SVG}
ET.register_namespace("", SVG)
ET.register_namespace("xlink", XLINK)
ET.register_namespace("inkscape", INK)


def node(parent, tag, **attrs):
    return ET.SubElement(parent, f"{{{SVG}}}{tag}", {k.replace("_", "-"): str(v) for k, v in attrs.items()})


def rect(parent, x, y, w, h, fill, stroke="none", rx=10):
    return node(parent, "rect", x=x, y=y, width=w, height=h, rx=rx,
                fill=fill, stroke=stroke, stroke_width=2.2)


def text(parent, x, y, value, size=22, weight=400, fill="#25272B", anchor="start"):
    el = node(parent, "text", x=x, y=y, font_size=size, font_weight=weight,
              fill=fill, text_anchor=anchor)
    el.text = value
    return el


def group(root, name):
    el = root.find(f".//s:g[@id='{name}']", NS)
    assert el is not None, name
    return deepcopy(el)


def geometry_signature(el):
    """Ignore authorized text/style edits, never path/image/branch geometry."""
    style = {"fill", "stroke", "stroke-width", "opacity"}
    return [(e.tag, sorted((k, v) for k, v in e.attrib.items() if k not in style))
            for e in el.iter() if not e.tag.endswith("}text")]


def polish(groups):
    for name in ("default-tree", "era-tree"):
        for el in groups[name].iter():
            tag = el.tag.split("}")[-1]
            if tag == "path":
                active = el.get("stroke") in {"#699BB3", "#688EA4", "#477D79"}
                el.set("stroke-width", "2.8" if el.get("stroke") == "#688EA4"
                       else "4.6" if active else "2.2")
            elif tag == "circle" and float(el.get("r")) > 2:
                el.set("stroke-width", "2.6" if el.get("r") == "17" else "2")
            elif tag == "text":
                if (el.text or "").strip() in {"1", "2", "3"}:
                    el.set("font-size", "24")
                    el.set("font-weight", "700")
                else:
                    el.text = "next"
                    el.set("font-size", "22")
                    el.set("fill", "#4F6070")

    # Stable positions identify text roles, so a second run does not depend on
    # the previous wording and never scales the same text twice.
    left = {
        776: ("Compare", "layouts", "Change found;", "not scored."),
        944: ("Check", "night scene", "Rain at night?", "Wet pavement?"),
        1112: ("Inspect", "details", "Windows?", "Reflections?"),
    }
    for el in groups["default-checks"].iter():
        tag = el.tag.split("}")[-1]
        if tag == "text":
            x, y = float(el.get("x")), float(el.get("y"))
            if y in (285, 309, 437, 460):
                el.text = left[x][(285, 309, 437, 460).index(y)]
                el.set("font-size", "28" if y < 326 else "23")
            elif y == 600:
                el.text = "Direction left undeveloped"
                el.set("font-size", "22")
                el.set("fill", "#4F6070")
            else:
                el.text = "B > A"
                el.set("font-size", "22")
                el.set("y", "496")
        elif tag in {"rect", "path"} and el.get("stroke"):
            el.set("stroke-width", "2.2")

    titles = ("Detect layout changes", "Use changes in scoring", "Weight by severity")
    diagnostics = (("Detected, but", "not scored."),
                   ("Scored, but", "underweighted."),
                   ("Larger changes,", "larger penalties."))
    for el in groups["era-revisions"].iter():
        tag = el.tag.split("}")[-1]
        if tag == "text":
            x, y = float(el.get("x")), float(el.get("y"))
            row = int((y - 152) // 152)
            if x == 1534:
                el.text = titles[row]
                el.set("font-size", "30")
            elif x == 1740:
                line = 0 if y - row * 152 < 230 else 1
                el.text = diagnostics[row][line]
                el.set("font-size", "27")
                el.set("fill", "#334B50")
            elif x == 1508:
                el.set("font-size", "22")
                el.set("font-weight", "700")
            else:
                el.text = "A > B" if row == 2 else "B > A"
                el.set("font-size", "22")
                el.set("y", str(275 + row * 152))
        elif tag in {"rect", "path", "circle"} and el.get("stroke"):
            el.set("stroke-width", "2.2")


def main():
    original = ET.fromstring(SOURCE.read_text())
    names = ("default-tree", "default-checks", "era-tree", "era-revisions")
    protected = {name: group(original, name) for name in names}
    before = {name: geometry_signature(el) for name, el in protected.items()}
    polish(protected)
    root = ET.Element(f"{{{SVG}}}svg", {
        "width": "2208", "height": "1056", "viewBox": "0 0 1840 880",
        "role": "img", "aria-labelledby": "title description",
        "data-layout": "shared-case-above-symmetric-method-panels",
        "data-polish": "compact-flat-hierarchy",
    })
    for tag in ("title", "desc"):
        root.append(deepcopy(original.find(f"s:{tag}", NS)))
    defs = node(root, "defs")
    style = node(defs, "style", id="flat-teaser-style")
    style.text = """
text { font-family: "TeX Gyre Heros", "Helvetica Neue", Arial, sans-serif; }
#default-tree text[fill="#FFFFFF"] { fill: #294E65; }
"""
    for marker in original.findall(".//s:marker", NS):
        defs.append(deepcopy(marker))
    rect(root, 0, 0, 1840, 880, "#FFFFFF", rx=0)
    rect(root, 8, 8, 1824, 220, "#FCF4EE", "#E8CEBD", 18)
    rect(root, 8, 242, 904, 608, "#F1F5FA", "#CDDAE7", 18)
    rect(root, 928, 242, 904, 608, "#F1F7F5", "#BAD6D1", 18)
    headings = node(root, "g", id="headings")
    for x, y, label, heading in (
        (37, 39, "a", "Task: evaluate edits"),
        (37, 275, "b", "Default setup"),
        (957, 275, "c", "IterEval: depth-first evolution"),
    ):
        node(headings, "circle", cx=x, cy=y, r=18, fill="#29577F")
        text(headings, x, y+9, label, 28, 700, "#FFFFFF", "middle")
        text(headings, x+33, y+8, heading, 32, 700)
    text(headings, 36, 94, "Make a rainy night.", 28)
    text(headings, 36, 128, "Keep the street layout", 28)
    text(headings, 36, 162, "and buildings unchanged.", 28)
    text(headings, 36, 205, "Each edit is scored separately.", 23, fill="#4F6070")
    text(headings, 70, 315, "Try a different direction", 28, fill="#4F6070")
    text(headings, 990, 315, "Continue one direction: layout fidelity", 28, fill="#477D79")
    text(headings, 458, 348, "Initial evaluation program", 23, fill="#4F6070", anchor="middle")
    text(headings, 1104, 348, "Initial evaluation program", 23, fill="#4F6070", anchor="middle")

    # Same full photographic viewports, uniformly reduced to a horizontal strip.
    photos = node(root, "g", id="task-photographs")
    for image_id, label, x in (("source-street", "Source", 466),
                               ("edit-a", "A", 606), ("edit-b", "B", 746)):
        old = original.find(f".//s:image[@id='{image_id}']", NS)
        clip = old.get("clip-path")[5:-1]
        wrapper = node(photos, "g", transform=f"translate({x} 54) scale(0.50) translate(-{old.get('x')} -{old.get('y')})")
        wrapper.append(deepcopy(original.find(f".//s:clipPath[@id='{clip}']", NS)))
        wrapper.append(deepcopy(old))
        text(headings, x+50, 40, label, 26, 700, anchor="middle")
    # Keep the original trade-off and opposing-ranking wording.
    tradeoff = node(root, "g", id="task-tradeoff")
    rect(tradeoff, 894, 65, 906, 38, "#E3EDE7", rx=6)
    rect(tradeoff, 894, 109, 906, 38, "#E5EDF5", rx=6)
    text(headings, 1310, 46, "A", 26, 700, anchor="middle")
    text(headings, 1650, 46, "B", 26, 700, anchor="middle")
    text(tradeoff, 914, 92, "Layout fidelity", 28, 700)
    text(tradeoff, 1310, 92, "Preserved", 28, 700, "#477D79", "middle")
    text(tradeoff, 1650, 92, "Wider street", 28, fill="#AC4D5D", anchor="middle")
    text(tradeoff, 914, 136, "Visual richness", 28, 700)
    text(tradeoff, 1310, 136, "Less vivid", 28, fill="#4F6070", anchor="middle")
    text(tradeoff, 1650, 136, "More vivid", 28, 700, "#29577F", "middle")
    rankings = node(root, "g", id="task-ranking-conflict")
    rect(rankings, 962, 165, 336, 44, "#DCEFE3", "#85B79C")
    rect(rankings, 1414, 165, 354, 44, "#F9DFDA", "#D9999F")
    text(rankings, 1130, 195, "Human: A > B", 28, 700, anchor="middle")
    text(rankings, 1355, 197, "≠", 29, 700, "#AC4F5D", "middle")
    text(rankings, 1591, 195, "Evaluator: B > A", 28, 700, anchor="middle")

    # Original branches retain all geometry; labels use the polish above.
    # Both roots align at y=365; branch descendants retain exact geometry.
    left = node(root, "g", id="default-placement",
                transform="translate(458 365) scale(1.04) translate(-944 -151)")
    # One calm surface groups the three plausible checks without turning them
    # into sequential method cards. Branches are drawn over it, unchanged.
    surfaces = node(left, "g", id="default-check-surface")
    rect(surfaces, 686, 253, 516, 257, "#FFFFFF", "#D4E0EA", 12)
    for x in (860, 1028):
        node(surfaces, "path", d=f"M{x} 280 V490", fill="none", stroke="#E3EAF0", stroke_width=1.6)
    left.append(protected["default-tree"])
    left.append(protected["default-checks"])
    right = node(root, "g", id="depth-placement", transform="translate(-240 214)")
    cards = node(right, "g", id="revision-card-surfaces")
    for y in (152, 304, 456):
        rect(cards, 1480, y, 544, 140, "#FFFFFF", "#A5C8BC", 12)
        rect(cards, 1481, y+1, 542, 36, "#E5F1EC", rx=11)
        rect(cards, 1481, y+20, 542, 17, "#E5F1EC", rx=0)
    right.append(protected["era-tree"])
    right.append(protected["era-revisions"])
    text(root, 990, 839, "Local ordering ≠ candidate acceptance.", 24, fill="#4F6070")
    disclosure = node(root, "g", id="disclosure")
    text(disclosure, 920, 873,
         "Illustrative search paths. Nodes are complete evaluation programs; images stay fixed.",
         22, fill="#4F6070", anchor="middle")
    for name in names:
        assert geometry_signature(group(root, name)) == before[name], name
    assert len(root.findall(".//s:image", NS)) == 9
    assert not root.findall(".//s:linearGradient", NS)
    if hasattr(ET, "indent"):
        ET.indent(root, space="  ")
    SOURCE.write_text('<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(root, encoding="unicode") + "\n")
    print("Polished text and stroke weights; branch geometry and all nine image crops unchanged.")


if __name__ == "__main__":
    main()
