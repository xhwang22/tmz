#!/usr/bin/env python3
"""Check the canonical overview exports and their inclusion in the paper.

Uses the standard library and Poppler. Print-size limitations are reported,
not silently cured by resizing the author-approved layout.
"""
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
NS = {"s": "http://www.w3.org/2000/svg"}
HREF = "{http://www.w3.org/1999/xlink}href"
REQUIRED = (
    "One direction, successive revisions", "Retain diagnostics",
    "Observed in execution", "Final scores unchanged.",
    "Agent’s next question", "Keep diagnostics after rollback",
    "No gain → keep best program", "End direction → start another",
    "Constructed example, not an observed trajectory",
    "Signal 1", "Signal 2", "Conflict → sample more", "+ random sample", "Reward",
)


def plain_pdf(path):
    return subprocess.check_output(["pdftotext", "-layout", str(path), "-"], text=True)


def normalized(text):
    return re.sub(r"\s+", " ", text).strip()


def audit(check_paper=False):
    manifest = json.loads((ROOT / "figures/overview.manifest.json").read_text())
    assert manifest["status"] == "canonical manuscript figure"
    assert manifest["constructed_illustration"] and not manifest["empirical_evidence"]
    assert manifest["canvas"] == [1840, 800]
    assert manifest["print_width_in"] == 5.4
    assert manifest["method_palette"] == ["#62AAA5", "#477D79"]
    for path, digest in manifest["files"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest, path
    assert hashlib.sha256((ROOT / manifest["source_image"]).read_bytes()).hexdigest() == manifest["source_sha256"]
    wrapper = (ROOT / "figures/overview.tex").read_text()
    assert r"\includegraphics[width=5.4in]{figures/overview.pdf}" in wrapper
    assert "tikzpicture" not in wrapper and "build/" not in wrapper
    svg = ET.parse(ROOT / "figures/overview.svg").getroot()
    assert manifest["connector_style"] == CONNECTOR_STYLE
    assert audit_markers(svg) > 0
    assert svg.get("viewBox") == "0 0 1840 800"
    labels = svg.findall(".//s:text", NS)
    assert [el.text for el in labels] == [label["text"] for label in manifest["text"]]
    assert len(labels) == 80
    assert manifest["mining_example"]["conflict"] == ["A > B", "B > A"]
    assert any(el.text == "≠" for el in labels), "Conflict must not rely on color alone"
    assert manifest["icon_cleanup"]["vector_text"] == ["Reward"]
    assert any(el.text == "Reward" for el in labels), "Reward must be vector text"
    assert svg.find(".//s:g[@id='refinement-speech-bubble']/s:path", NS) is not None, "Missing complete vector bubble"
    images = svg.findall(".//s:image", NS)
    assert len(images) == len(manifest["embedded_images"])
    for el, record in zip(images, manifest["embedded_images"]):
        href = el.get(HREF, "")
        assert href.startswith("data:image/png;base64,")
        data = base64.b64decode(href.split(",", 1)[1])
        assert hashlib.sha256(data).hexdigest() == record["sha256"]
        assert list(struct.unpack(">II", data[16:24])) == record["pixels"]
        assert [float(el.get(k)) for k in ("x", "y", "width", "height")] == record["box"]
    pdf = ROOT / "figures/overview.pdf"
    text = normalized(plain_pdf(pdf))
    for label in REQUIRED:
        assert label in text, f"Missing PDF label: {label}"
    info = subprocess.check_output(["pdfinfo", str(pdf)], text=True)
    dimensions = re.search(r"Page size:\s+([\d.]+) x ([\d.]+) pts", info)
    assert dimensions and abs(float(dimensions[1]) - 388.8) < .01
    assert abs(float(dimensions[2]) - 388.8 * 800 / 1840) < .01
    fonts = subprocess.check_output(["pdffonts", str(pdf)], text=True).splitlines()[2:]
    assert fonts and all("Type 3" not in row and row.split()[-5] == "yes" for row in fonts)
    for filename in ("method.tex", "introduction.tex"):
        source = (ROOT / "sections" / filename).read_text()
        assert r"\ref{fig:overview}b" in source
        assert r"\ref{fig:overview}c" not in source
    if check_paper:
        pages = plain_pdf(ROOT / "paper.pdf").split("\f")
        matches = [(i + 1, normalized(page)) for i, page in enumerate(pages)
                   if "Retain diagnostics" in page]
        assert len(matches) == 1, "Canonical Fig2 missing or repeated in compiled paper"
        page_number, page = matches[0]
        assert "Figure 2: IterEval" in page
        assert all(label in page for label in REQUIRED), "Paper does not contain all overview labels"
        print(f"Compiled Figure 2 verified on page {page_number}.")
    sizes = manifest["font_size_pt"]
    ppis = [record["effective_ppi"] for record in manifest["embedded_images"]]
    print(f"Overview: {len(labels)} vector labels; {len(images)} embedded pictograms; canonical hashes and fonts verified.")
    print(f"Print limits: labels {sizes[0]:.1f}–{sizes[1]:.1f} pt; pictograms {min(ppis):.0f}–{max(ppis):.0f} PPI.")


if __name__ == "__main__":
    audit(check_paper=True)
