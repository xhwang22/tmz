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
    assert min(map(float, re.findall(r"\\fontsize\{([0-9.]+)\}", layout))) >= 7
    print_ppis = []
    for relative, digest in info["paper_photos"].items():
        raw = (ROOT / relative).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == digest, relative
        w, h = struct.unpack(">II", raw[16:24])
        width = re.search(r"\\includegraphics\[width=([0-9.]+)cm\]\{" + re.escape(relative) + r"\}", layout)
        assert width, relative
        print_ppis.append(w * 2.54 / float(width[1]))
    assert len(print_ppis) == 3 and min(print_ppis) >= 300
    root = ET.fromstring(source.read_text())
    scale = info["print_width_in"] / float(root.get("viewBox").split()[2])
    ppis, font_pts = [], []
    for el in root.iter():
        if el.tag.endswith("}text"):
            font_pts.append(float(el.get("font-size")) * scale * 72)
        if not el.tag.endswith("}image"):
            continue
        raw = base64.b64decode(el.get("{http://www.w3.org/1999/xlink}href").split(",", 1)[1])
        w, h = struct.unpack(">II", raw[16:24])
        # 'slice' crops, rather than stretching, each inset to fill its viewport.
        ppi = min(w / (float(el.get("width"))*scale), h / (float(el.get("height"))*scale))
        ppis.append(ppi)
    assert len(ppis) == 9
    fonts = subprocess.check_output(["pdffonts", str(ROOT / "figures/teaser.pdf")], text=True)
    assert "Type 3" not in fonts
    for line in fonts.splitlines()[2:]:
        assert re.search(r"\byes\s+yes\s+yes\b", line), line
    print(f"Reference SVG: nine unchanged images, embedded PDF fonts; not the print layout.")
    print(f"Paper teaser: native labels at least 7 pt; three unchanged photos at {min(print_ppis):.0f}–{max(print_ppis):.0f} PPI.")
    assert min(ppis) >= 300, "Photographic insets below 300 PPI"
    return ppis


if __name__ == "__main__":
    audit()
