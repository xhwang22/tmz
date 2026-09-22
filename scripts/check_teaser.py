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
