#!/usr/bin/env python3
"""Polish the shared-case teaser while preserving its search-tree topology.

Spread panel b horizontally; lower panel c's bottom two fork points.
Preserve node positions and all solid/dashed branch semantics.
Retain photographic crops and match the overview's flat surface hierarchy.
The script is idempotent and overwrites the stable source, not a new candidate.
"""
from copy import deepcopy
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from PIL import ImageFont
from figure_fonts import SVG_FAMILY, font_path
from figure_connectors import STYLE as CONNECTOR_STYLE, arrow_marker

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "figures/candidates/teaser-v6-paper-wording/teaser.svg"
SVG = "http://www.w3.org/2000/svg"
XLINK = "http://www.w3.org/1999/xlink"
INK = "http://www.inkscape.org/namespaces/inkscape"
NS = {"s": SVG}
SURFACE_STYLE = "overview-paper-symmetric-tree"
BODY = "#25272B"
NOTE = "#707982"
BLUE = "#29577F"
GREEN = "#477D79"
PAPER = "#FFFEFA"
PHOTO_EDGE = "#AEB7B3"
ET.register_namespace("", SVG)
ET.register_namespace("xlink", XLINK)
ET.register_namespace("inkscape", INK)


def node(parent, tag, **attrs):
    return ET.SubElement(parent, f"{{{SVG}}}{tag}", {k.replace("_", "-"): str(v) for k, v in attrs.items()})


def rect(parent, x, y, w, h, fill, stroke="none", rx=10, stroke_width=1.5):
    return node(parent, "rect", x=x, y=y, width=w, height=h, rx=rx,
                fill=fill, stroke=stroke, stroke_width=stroke_width)


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
    style = {"fill", "stroke", "stroke-width", "opacity", "stroke-dasharray",
             "stroke-dashoffset", "stroke-linecap", "stroke-linejoin"}
    return [(e.tag, sorted((k, v) for k, v in e.attrib.items() if k not in style))
            for e in el.iter() if not e.tag.endswith("}text")]


def restore_layout(el):
    """Recover base coordinates before applying the stable layout again."""
    for item in el.iter():
        for key in list(item.attrib):
            if key.startswith("data-base-"):
                item.set(key[len("data-base-"):], item.attrib.pop(key))


def place(el, **attrs):
    for key, value in attrs.items():
        el.set(f"data-base-{key}", el.get(key))
        el.set(key, f"{value:g}" if isinstance(value, (int, float)) else value)


def lower_depth_forks(tree):
    """Share more of the parent stem before the two lower side branches fan out.

    Only four paths change. Their sources, targets and arrowheads stay fixed;
    a vertical prefix keeps the connection to the original parent explicit.
    The visible fan is 50 units high, matching the top-level side branches.
    """
    paths = {
        f"M1344 {start} C1344 {start+21} {x} {start+17} {x} {end}":
        f"M1344 {start} V{end-50} C1344 {end-29} {x} {end-33} {x} {end}"
        for start, end in ((241, 353), (393, 505)) for x in (1250, 1438)
    }
    changed = 0
    for el in tree.findall("s:path", NS):
        if el.get("d") in paths:
            assert el.get("stroke") == "#B8CAC8"
            place(el, d=paths[el.get("d")])
            changed += 1
    assert changed == 4, "Expected two pairs of lower unexplored branches"


def normalize_revisions(revisions):
    """Unwrap layout-only translations and remove redundant card numbers."""
    children = []
    for el in revisions:
        children.extend(list(el) if el.get("data-layout-wrapper") else [el])
    revisions[:] = children
    restore_layout(revisions)
    for el in list(revisions):
        if (el.tag.endswith("}circle") and el.get("cx") == "1508") or (
                el.tag.endswith("}text") and el.get("x") == "1508"):
            revisions.remove(el)


def arrange_revisions(revisions):
    """Match the approved symmetric preview without changing image crops."""
    parts = list(revisions)
    assert len(parts) == 27
    revisions[:] = []
    for i in range(3):
        title, clip, photo, edge, first, second, badge, sign, label = parts[i*9:(i+1)*9]
        y = 222 + 152*i
        place(title, x=1500, y=y-40)
        revisions.append(title)
        picture = node(revisions, "g", data_layout_wrapper="photo", transform="translate(0 2)")
        picture.extend((clip, photo, edge))
        place(first, x=1744, y=y-3)
        place(second, x=1744, y=y+23)
        revisions.extend((first, second))
        outcome = node(revisions, "g", data_layout_wrapper="outcome", transform="translate(0 1)")
        outcome.extend((badge, sign, label))


def widen_default(groups):
    """Wider sibling spacing, not a stretched image, font or node shape."""
    def xwide(x):
        return 944 + (float(x) - 944) * 264 / 168

    for el in groups["default-tree"].iter():
        tag = el.tag.split("}")[-1]
        if tag == "circle":
            place(el, cx=xwide(el.get("cx")))
        elif tag == "text":
            place(el, x=xwide(el.get("x")))
        elif tag == "path":
            # These tree paths contain only absolute M/C/H/V commands.
            tokens = re.findall(r"[A-Za-z]|-?\d+(?:\.\d+)?", el.get("d"))
            output, command, index = [], None, 0
            descendant = tokens[:1] == ["M"] and tokens[2] == "518"
            for token in tokens:
                if token.isalpha():
                    assert token in {"M", "C", "H", "V"}, token
                    command, index = token, 0
                    output.append(token)
                    continue
                value = float(token)
                is_x = command == "H" or (command != "V" and index % 2 == 0)
                if is_x:
                    value = xwide(value)
                elif descendant:
                    value = {518: 533, 539: 543, 535: 541, 547: 550}.get(value, value)
                output.append(f"{value:g}")
                index += 1
            place(el, d=" ".join(output))

    for el in groups["default-checks"].iter():
        tag = el.tag.split("}")[-1]
        if tag == "text":
            x, y = float(el.get("x")), float(el.get("y"))
            # A single heading fits each wider column; same wording and order.
            if y == 285:
                el.text = {776: "Compare layouts", 944: "Check rain effects",
                           1112: "Inspect details"}[x]
            elif y == 309:
                el.text = ""
            place(el, x=xwide(x) if x != 783.5 else 687.5,
                  y={437: 451, 460: 478, 496: 510}.get(y, y))
            if y in (437, 460):
                el.set("font-size", "26")
            if y in (285, 437, 460):
                font = ImageFont.truetype(str(font_path("bold" if y == 285 else "regular")),
                                          int(el.get("font-size")))
                assert font.getlength(el.text) <= 245, ("Default annotation overflow", el.text)
        elif tag in {"image", "rect"} and el.get("y") == "326":
            # Uniform 1.1x enlargement preserves the crop and >=300 source PPI.
            center = float(el.get("x")) + 65
            place(el, x=xwide(center)-71.5, y=318.75, width=143, height=93.5)
        elif tag == "rect" and el.get("y") == "474":
            place(el, x=616, y=488)
        elif tag == "path":
            assert el.get("d") == "M722 485.5 l6 6 M728 485.5 l-6 6"
            place(el, d="M626 499.5 l6 6 M632 499.5 l-6 6")


def polish(groups):
    for name in ("default-tree", "era-tree"):
        for el in groups[name].iter():
            tag = el.tag.split("}")[-1]
            if tag == "path":
                active = el.get("stroke") in {"#699BB3", "#688EA4", "#477D79"}
                el.set("stroke-width", "2.3" if el.get("stroke") == "#688EA4"
                       else "3.5" if active else "1.9")
                el.set("stroke-linecap", "round")
                el.set("stroke-linejoin", "round")
                if el.get("stroke-dasharray"):
                    # Longer gaps remain visible after round caps and PDF
                    # reduction. Preserve dashed/solid semantics exactly.
                    el.set("stroke-dasharray", "7 6" if el.get("stroke") == "#688EA4"
                           else "3 6" if active else "2 5")
            elif tag == "circle" and float(el.get("r")) > 2:
                el.set("stroke-width", "2.6" if el.get("r") == "17" else "2")
            elif tag == "text":
                if (el.text or "").strip() in {"1", "2", "3"}:
                    el.set("font-size", "24")
                    el.set("font-weight", "700")
                else:
                    el.text = "next"
                    el.set("font-size", "22")
                    el.set("fill", NOTE)

    # Stable positions identify text roles, so a second run does not depend on
    # the previous wording and never scales the same text twice.
    left = {
        776: ("Compare", "layouts", "Wider street found;", "score unchanged."),
        944: ("Check", "rain effects", "Score rainfall and", "wet-road cues."),
        1112: ("Inspect", "details", "Check windows", "and reflections."),
    }
    for el in groups["default-checks"].iter():
        tag = el.tag.split("}")[-1]
        if tag == "text":
            x, y = float(el.get("x")), float(el.get("y"))
            if y in (285, 309, 437, 460):
                el.text = left[x][(285, 309, 437, 460).index(y)]
                el.set("font-size", "28" if y < 326 else "23")
                el.set("fill", BLUE if y < 326 else BODY)
            elif y == 600:
                el.text = "Layout finding left unused"
                el.set("font-size", "22")
                el.set("fill", NOTE)
            else:
                el.text = "B > A"
                el.set("font-size", "22")
                el.set("y", "496")
        elif tag == "rect" and el.get("stroke"):
            el.set("stroke-width", "1.5")
            if el.get("y") == "326":
                el.set("stroke", PHOTO_EDGE)

    titles = ("Detect layout changes", "Penalize layout changes", "Penalize major errors more")
    diagnostics = (("Wider street found;", "score unchanged."),
                   ("Same penalty for", "small and large edits."),
                   ("Street widening", "outweighs extra detail."))
    for el in groups["era-revisions"].iter():
        tag = el.tag.split("}")[-1]
        if tag == "text":
            x, y = float(el.get("x")), float(el.get("y"))
            row = int((y - 152) // 152)
            if x == 1534:
                el.text = titles[row]
                el.set("font-size", "30")
                el.set("fill", GREEN)
                font = ImageFont.truetype(str(font_path("bold")), 30)
                assert font.getlength(el.text) <= 475, ("Revision heading overflow", el.text)
            elif x == 1740:
                line = 0 if y - row * 152 < 230 else 1
                el.text = diagnostics[row][line]
                el.set("font-size", "27")
                el.set("fill", BODY)
                font = ImageFont.truetype(str(font_path()), 27)
                assert font.getlength(el.text) <= 272, ("Revision annotation overflow", el.text)
            elif x == 1508:
                el.set("font-size", "22")
                el.set("font-weight", "700")
            else:
                el.text = "A > B" if row == 2 else "B > A"
                el.set("font-size", "22")
                el.set("y", str(275 + row * 152))
        elif tag in {"rect", "circle"} and el.get("stroke"):
            el.set("stroke-width", "1.5")
            if tag == "rect" and float(el.get("y")) in {194, 346, 498}:
                el.set("stroke", PHOTO_EDGE)


def main():
    original = ET.fromstring(SOURCE.read_text())
    names = ("default-tree", "default-checks", "era-tree", "era-revisions")
    protected = {name: group(original, name) for name in names}
    normalize_revisions(protected["era-revisions"])
    for el in protected.values():
        restore_layout(el)
    before = {name: geometry_signature(el) for name, el in protected.items()}
    polish(protected)
    for name in names:
        assert geometry_signature(protected[name]) == before[name], name
    widen_default(protected)
    lower_depth_forks(protected["era-tree"])
    arrange_revisions(protected["era-revisions"])
    root = ET.Element(f"{{{SVG}}}svg", {
        "width": "2208", "height": "1056", "viewBox": "0 0 1840 880",
        "role": "img", "aria-labelledby": "title description",
        "data-layout": "shared-case-above-symmetric-method-panels",
        "data-polish": "compact-flat-wide-default",
        "data-surface-style": SURFACE_STYLE,
        "data-depth-forks": "lower-two-fans-50-units",
        "data-node-edit-mapping": "symmetric-tree-adjacent-cards",
        "data-step-wording": "concrete-layout-diagnostics",
        "data-connectors": CONNECTOR_STYLE,
    })
    for tag in ("title", "desc"):
        root.append(deepcopy(original.find(f"s:{tag}", NS)))
    defs = node(root, "defs")
    style = node(defs, "style", id="flat-teaser-style")
    style.text = """
text { font-family: FONT_FAMILY; }
#default-tree text[fill="#FFFFFF"] { fill: #294E65; }
""".replace("FONT_FAMILY", SVG_FAMILY)
    for identifier, color, length, height in (
        ("blueArrow", "#699BB3", 12, 10),
        ("orderArrow", "#688EA4", 11, 9),
        ("roseArrow", "#477D79", 12, 10),
        ("ghostBlueArrow", "#AFBFCC", 9, 7.5),
        ("ghostRoseArrow", "#B8CAC8", 9, 7.5),
    ):
        defs.append(ET.fromstring(arrow_marker(identifier, color, length, height)
                                 .replace('<marker ', f'<marker xmlns="{SVG}" ', 1)))
    rect(root, 0, 0, 1840, 880, "#FFFFFF", rx=0)
    rect(root, 8, 8, 1824, 220, "#FCF4EE", "#E8CEBD", 25)
    rect(root, 8, 242, 904, 608, "#F1F5FA", "#CDDAE7", 25)
    rect(root, 928, 242, 904, 608, "#F1F7F5", "#BAD6D1", 25)
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
    text(headings, 36, 205, "Each edit is scored separately.", 23, fill=NOTE)
    text(headings, 70, 315, "Try a different direction", 28, fill=BLUE)
    text(headings, 990, 315, "Continue one direction: layout fidelity", 28, fill="#477D79")
    text(headings, 458, 348, "Initial evaluation program", 23, fill=NOTE, anchor="middle")
    text(headings, 1104, 348, "Initial evaluation program", 23, fill=NOTE, anchor="middle")

    # Same full photographic viewports, uniformly reduced to a horizontal strip.
    photos = node(root, "g", id="task-photographs")
    for image_id, label, x in (("source-street", "Source", 466),
                               ("edit-a", "A", 606), ("edit-b", "B", 746)):
        old = original.find(f".//s:image[@id='{image_id}']", NS)
        clip = old.get("clip-path")[5:-1]
        # The mount surrounds the full viewport; photo data and clips stay fixed.
        rect(photos, x-3, 51, 106, 155, PAPER, PHOTO_EDGE, 5)
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
    text(tradeoff, 1310, 136, "Less vivid", 28, fill=BODY, anchor="middle")
    text(tradeoff, 1650, 136, "More vivid", 28, 700, "#29577F", "middle")
    rankings = node(root, "g", id="task-ranking-conflict")
    rect(rankings, 962, 165, 336, 44, "#DCEFE3", "#85B79C")
    rect(rankings, 1414, 165, 354, 44, "#F9DFDA", "#D9999F")
    text(rankings, 1130, 195, "Human: A > B", 28, 700, anchor="middle")
    text(rankings, 1355, 197, "≠", 29, 700, "#AC4F5D", "middle")
    text(rankings, 1591, 195, "Evaluator: B > A", 28, 700, anchor="middle")

    # Both roots align at y=365. Panel b spreads sibling columns without
    # changing topology; panel c only lowers its two lower side-fork points.
    left = node(root, "g", id="default-placement",
                transform="translate(458 365) scale(1.04) translate(-944 -151)")
    # One calm surface groups the three plausible checks without turning them
    # into sequential method cards. Branches keep their existing semantics.
    surfaces = node(left, "g", id="default-check-surface")
    rect(surfaces, 554, 253, 780, 272, PAPER, "#CDDAE7", 12)
    for x in (812, 1076):
        node(surfaces, "path", d=f"M{x} 273 V505", fill="none", stroke="#E3EAF0", stroke_width=1.5)
    left.append(protected["default-tree"])
    left.append(protected["default-checks"])
    right = node(root, "g", id="depth-placement", transform="translate(-240 214)")
    # Complete symmetric branches remain separate from adjacent edit details.
    # No duplicate numbered badges, one-sided branches, tabs or guide lines.
    cards = node(right, "g", id="revision-card-surfaces")
    for y in (152, 304, 456):
        rect(cards, 1480, y, 558, 140, PAPER, "#B7D0C7", 12)
    right.append(protected["era-tree"])
    right.append(protected["era-revisions"])
    text(root, 990, 839, "Local ordering ≠ candidate acceptance.", 24, fill=NOTE)
    disclosure = node(root, "g", id="disclosure")
    text(disclosure, 920, 873,
         "Illustrative search paths. Nodes are complete evaluation programs; images stay fixed.",
         22, fill=NOTE, anchor="middle")
    for name in ("era-tree", "era-revisions"):
        restored = group(root, name)
        if name == "era-revisions":
            normalize_revisions(restored)
        restore_layout(restored)
        assert geometry_signature(restored) == before[name], name
    assert len(root.findall(".//s:image", NS)) == 9
    assert not root.findall(".//s:linearGradient", NS)
    if hasattr(ET, "indent"):
        ET.indent(root, space="  ")
    SOURCE.write_text('<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(root, encoding="unicode") + "\n")
    print("Approved symmetric branches and adjacent edit cards retained; tree, text and photos preserved.")


if __name__ == "__main__":
    main()
