#!/usr/bin/env python3
"""Audit the mixed vector/raster teaser at its actual manuscript print size."""
import base64
import hashlib
import json
from pathlib import Path
import re
import struct
import subprocess
import xml.etree.ElementTree as ET
from figure_connectors import STYLE as CONNECTOR_STYLE, audit_markers

ROOT = Path(__file__).resolve().parents[1]


def audit():
    info = json.loads((ROOT / "figures/teaser.manifest.json").read_text())
    for name, digest in info["files"].items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
    source = ROOT / info["source"]
    assert source.read_bytes() == (ROOT / "figures/teaser.svg").read_bytes()
    assert hashlib.sha256(source.read_bytes()).hexdigest() == info["source_sha256"]
    raw_source = ROOT / info["image_source"]
    assert hashlib.sha256(raw_source.read_bytes()).hexdigest() == info["image_source_sha256"]
    assert info["constructed_illustration"] and not info["empirical_evidence"]
    layout = (ROOT / info["paper_layout"]).read_text()
    assert "scalebox" not in layout and "resizebox" not in layout
    assert info["paper_graphic"] == "figures/teaser.pdf"
    width = re.search(r"\\includegraphics\[width=([0-9.]+)in\]\{figures/teaser.pdf\}", layout)
    assert width and abs(float(width[1]) - info["print_width_in"]) < 1e-6
    root = ET.fromstring(source.read_text())
    assert info["connector_style"] == CONNECTOR_STYLE
    assert audit_markers(root) == info["connector_revision"]["arrow_count"]
    ns = {"s": "http://www.w3.org/2000/svg"}
    if info.get("branch_revision"):
        assert root.get("data-depth-forks") == info["branch_revision"]["style"]
        tree = root.find(".//s:g[@id='era-tree']", ns)
        paths = tree.findall("s:path[@data-base-d]", ns)
        assert len(paths) == 4
        expected = {
            f"M1344 {start} V{end-50} C1344 {end-29} {x} {end-33} {x} {end}":
            f"M1344 {start} C1344 {start+21} {x} {start+17} {x} {end}"
            for start, end in ((241, 353), (393, 505)) for x in (1250, 1438)
        }
        assert {el.get("d"): el.get("data-base-d") for el in paths} == expected
        assert all(el.get("marker-end") == "url(#ghostRoseArrow)" for el in paths)
        main = [el.get("d") for el in tree.findall("s:path", ns) if el.get("stroke") == "#477D79"]
        assert main == ["M1344 151 V201", "M1344 241 V352", "M1344 393 V504", "M1344 545 V586"]
        assert {float(el.get("cy")) for el in tree.findall("s:circle", ns) if el.get("r") == "17"} == {222, 374, 526}
        print("Lower forks: four side paths have 50-unit fans; parent connections and main spine retained.")
    if info.get("node_edit_mapping", {}).get("style") == "symmetric-tree-adjacent-cards":
        assert root.get("data-node-edit-mapping") == "symmetric-tree-adjacent-cards"
        assert root.get("data-review-only") is None
        for name in ("node-edit-leaders", "node-edit-rows", "direction-surface", "expanded-program-surfaces"):
            assert root.find(f".//s:g[@id='{name}']", ns) is None, name
        tree = root.find(".//s:g[@id='era-tree']", ns)
        revisions = root.find(".//s:g[@id='era-revisions']", ns)
        assert not revisions.findall(".//s:circle", ns)
        assert not any(el.text in {"1", "2", "3"} for el in revisions.findall(".//s:text", ns))
        cards = root.findall(".//s:g[@id='revision-card-surfaces']/s:rect", ns)
        assert len(cards) == 3
        for i, y in enumerate((222, 374, 526)):
            xs = sorted(float(el.get("cx")) for el in tree.findall("s:circle", ns)
                        if float(el.get("cy")) == y and el.get("fill") == "#FFFFFF")
            assert xs == ([1250, 1297, 1391, 1438] if i == 0 else [1250, 1438])
            assert all(a+b == 2*1344 for a, b in zip(xs, reversed(xs)))
            assert float(cards[i].get("y")) + 70 == y
            assert cards[i].get("x") == "1480" and cards[i].get("width") == "558"
            assert cards[i].get("fill") == "#FFFEFA" and cards[i].get("stroke-width") == "1.5"
        panels = [el for el in root.findall("s:rect", ns) if el.get("stroke") != "none"]
        assert len(panels) == 3 and all(el.get("rx") == "25" for el in panels)
        for tag in ("linearGradient", "radialGradient", "filter"):
            assert not root.findall(f".//s:{tag}", ns)
        print("Approved Fig1: complete symmetric branches, adjacent cards, no duplicate badges or correspondence guides.")
    elif info.get("node_edit_mapping"):
        assert root.get("data-node-edit-mapping") == info["node_edit_mapping"]["style"]
        assert root.find(".//s:g[@id='node-edit-leaders']", ns) is None
        rows = root.find(".//s:g[@id='node-edit-rows']", ns)
        assert rows is not None and rows.get("data-role") == "annotation-row-grouping"
        bands = rows.findall("s:rect", ns)
        assert len(bands) == 3 and not rows.findall("s:path", ns)
        tree = root.find(".//s:g[@id='era-tree']", ns)
        revisions = root.find(".//s:g[@id='era-revisions']", ns)
        cards = root.findall(".//s:g[@id='revision-card-surfaces']/s:rect", ns)
        badges = revisions.findall("s:circle[@cx='1480']", ns)
        numbers = revisions.findall("s:text[@x='1480']", ns)
        headings = revisions.findall("s:text[@x='1500']", ns)
        photos = revisions.findall(".//s:image", ns)
        assert len(cards) == len(badges) == len(numbers) == len(headings) == len(photos) == 3
        assert [el.text for el in numbers] == ["1", "2", "3"]
        for i, y in enumerate((222, 374, 526)):
            assert tree.find(f"s:circle[@cx='1344'][@cy='{y}'][@r='17']", ns) is not None
            assert float(cards[i].get("y")) + float(cards[i].get("height"))/2 == y
            assert float(badges[i].get("cy")) == y
            assert badges[i].get("cx") == cards[i].get("x")
            assert 6 <= float(numbers[i].get("y")) - y <= 7
            assert photos[i].get("x") == headings[i].get("x")
            assert float(photos[i].get("y")) == y - 28
            band = bands[i]
            assert band.get("stroke") == "none" and band.get("fill") == "#E0EEEA"
            assert float(band.get("y")) + float(band.get("height"))/2 == y
            assert float(band.get("x")) < 1344 - 17
            assert float(band.get("x")) + float(band.get("width")) >= 1480 + 544
        print("Node/edit correspondence: aligned numbered docks and pale row surfaces; no annotation lines.")
    if info.get("surface_polish", {}).get("style") == "overview-paper-and-direction-surfaces":
        assert root.get("data-surface-style") == info["surface_polish"]["style"]
        direction = root.find(".//s:g[@id='direction-surface']/s:rect", ns)
        assert direction is not None and direction.get("fill") == "#E7F2EF"
        cards = root.findall(".//s:g[@id='revision-card-surfaces']/s:rect", ns)
        assert len(cards) == 3 and all(el.get("fill") == "#FFFEFA" for el in cards)
        assert all(el.get("stroke-width") == "1.5" for el in cards)
        panels = [el for el in root.findall("s:rect", ns) if el.get("stroke") != "none"]
        assert len(panels) == 3
        assert all(el.get("rx") == "25" and el.get("stroke-width") == "1.5" for el in panels)
        for tag in ("linearGradient", "radialGradient", "filter"):
            assert not root.findall(f".//s:{tag}", ns), f"Unexpected surface effect: {tag}"
        print("Surface hierarchy: overview-matched panels, one direction surface and three paper cards.")
    tradeoff = root.find(".//s:g[@id='task-tradeoff']", ns)
    rankings = root.find(".//s:g[@id='task-ranking-conflict']", ns)
    if info.get("panel_a_revision"):
        assert tradeoff is not None and rankings is not None
        assert [el.text for el in tradeoff.findall("s:text", ns)] == [
            "Layout fidelity", "Preserved", "Wider street",
            "Visual richness", "Less vivid", "More vivid",
        ]
        assert [el.text for el in rankings.findall("s:text", ns)] == [
            "Human: A > B", "≠", "Evaluator: B > A",
        ]
        print("Panel a: qualitative trade-off and opposite overall rankings are explicit.")
    if info.get("step_wording_revision"):
        text = subprocess.check_output(["pdftotext", "-layout", str(ROOT / "figures/teaser.pdf"), "-"], text=True)
        for label in info["step_wording_revision"]["depth_steps"]:
            assert label in text, f"Missing revised step in PDF: {label}"
        labels = [el.text for el in root.findall(".//s:text", ns)]
        assert "Same penalty for" in labels and "small and large edits." in labels
        assert "outweighs extra detail." in labels
        assert "underweighted." not in labels and "not scored." not in labels
        assert "TeX Gyre Pagella" in source.read_text(), "Layout regeneration reverted figure typography"
        print("Step annotations: concrete layout findings, penalty limitation and task trade-off verified.")
    scale = info["print_width_in"] / float(root.get("viewBox").split()[2])
    ppis, font_pts = [], []
    parents = {child: parent for parent in root.iter() for child in parent}
    def local_scale(el):
        factor = 1.0
        while el is not None:
            transform = el.get("transform", "")
            # This source uses translations and uniform scales only.
            for match in re.finditer(r"scale\(\s*([0-9.]+)\s*\)", transform):
                factor *= float(match[1])
            assert not re.search(r"matrix\(|rotate\(|skew", transform), transform
            el = parents.get(el)
        return factor
    for el in root.iter():
        effective_scale = scale * local_scale(el)
        if el.tag.endswith("}text"):
            font_pts.append(float(el.get("font-size")) * effective_scale * 72)
        if not el.tag.endswith("}image"):
            continue
        raw = base64.b64decode(el.get("{http://www.w3.org/1999/xlink}href").split(",", 1)[1])
        w, h = struct.unpack(">II", raw[16:24])
        # 'slice' crops, rather than stretching, each inset to fill its viewport.
        ppi = min(w / (float(el.get("width"))*effective_scale), h / (float(el.get("height"))*effective_scale))
        ppis.append(ppi)
    assert len(ppis) == 9
    fonts = subprocess.check_output(["pdffonts", str(ROOT / "figures/teaser.pdf")], text=True)
    assert "Type 3" not in fonts
    for line in fonts.splitlines()[2:]:
        assert re.search(r"\byes\s+yes\s+yes\b", line), line
    print(f"Paper teaser: preserved search layout, nine images at {min(ppis):.0f}–{max(ppis):.0f} PPI; embedded PDF fonts.")
    if min(font_pts) < 7:
        print(f"Readability warning: vector text/symbols are {min(font_pts):.1f}–{max(font_pts):.1f} pt at print size; small-label limitation remains.")
    assert min(ppis) >= 300, "Photographic insets below 300 PPI"
    return ppis


if __name__ == "__main__":
    audit()
