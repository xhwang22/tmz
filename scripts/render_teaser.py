#!/usr/bin/env python3
"""Integrate the author-edited v6 teaser; change method colors, not its content.

The self-contained SVG is the source of truth: do not regenerate it from an
older wording profile. This exporter checks that all text, geometry and nine
embedded images survive recoloring. No image generation or data fabrication.
"""
import base64
import hashlib
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

import cairosvg

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "figures/candidates/teaser-v6-paper-wording/teaser.svg"
OUT = ROOT / "figures"
# Same lake green as scripts/render_c1_landscape.py; red stays an error signal.
PALETTE = {
    "#FAF0F3": "#EFF6F5", "#D8AAB8": "#A6CCC8",
    "#DD7389": "#62AAA5", "#C2667B": "#477D79",
    "#AD5066": "#477D79", "#B8B6C3": "#B8CAC8",
    "#EED8E1": "#CADFDC", "#E3B8C5": "#B5D4D0", "#D8B6C1": "#B5D4D0",
}
NS = {"s": "http://www.w3.org/2000/svg"}
HREF = "{http://www.w3.org/1999/xlink}href"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def signature(svg):
    root = ET.fromstring(svg)
    return [(el.tag, el.text, tuple(sorted((k, v) for k, v in el.attrib.items()
             if k not in {"fill", "stroke"}))) for el in root.iter()]


def main():
    original = SOURCE.read_text()
    svg = re.sub(r'(?<=")#[0-9A-Fa-f]{6}(?=")',
                 lambda m: PALETTE.get(m[0].upper(), m[0]), original)
    # The original shared one rose stroke with an error badge: retain its red.
    svg = re.sub(r'(<circle[^>]*fill="#C65368"[^>]*stroke=")[^"]+("[^>]*>)',
                 r'\g<1>#AD5066\2', svg)
    # Dark node numerals have higher contrast on the lake-green method fill.
    def method_numerals(match):
        return re.sub(r'(<text[^>]*fill=")#FFFFFF("[^>]*>[123]</text>)',
                      r'\g<1>#234B49\2', match[0])
    svg = re.sub(r'<g id="era-(?:tree|revisions)"[\s\S]*?</g>', method_numerals, svg)
    assert signature(original) == signature(svg), "Recoloring changed content"
    doc = ET.fromstring(svg)
    images = doc.findall(".//s:image", NS)
    assert len(images) == 9
    assert all(el.get(HREF, "").startswith("data:image/png;base64,") for el in images)
    # Reproducible outputs include the user's editable source and both previews.
    SOURCE.write_text(svg)
    (OUT / "teaser.svg").write_text(svg)
    for directory in (SOURCE.parent, OUT):
        cairosvg.svg2pdf(bytestring=svg.encode(), write_to=str(directory / "teaser.pdf"))
        cairosvg.svg2png(bytestring=svg.encode(), write_to=str(directory / "teaser.png"))
    cairosvg.svg2png(bytestring=svg.encode(), write_to=str(SOURCE.parent / "teaser-2x.png"), scale=2)
    asset_manifest = json.loads((SOURCE.parent / "manifest.json").read_text())
    asset_manifest.update({"canonical_integration": True, "method_accent": "#62AAA5",
                           "palette_check": "text, geometry and embedded images unchanged"})
    (SOURCE.parent / "manifest.json").write_text(json.dumps(asset_manifest, indent=2) + "\n")
    info = {
        "source": str(SOURCE.relative_to(ROOT)), "source_sha256": digest(svg.encode()),
        "author_wording_preserved": True, "geometry_preserved": True,
        "method_accent": "#62AAA5", "error_status_colors_preserved": True,
        "empirical_evidence": False, "constructed_illustration": True,
        "new_generation": False, "print_width_in": 5.4,
        "paper_layout": "figures/teaser.tex",
        "paper_graphic": "figures/teaser.pdf",
        "image_source": asset_manifest["source"],
        "image_source_sha256": asset_manifest["source_sha256"],
        "embedded_images": [{"sha256": digest(base64.b64decode(el.get(HREF).split(",", 1)[1])),
                              "svg_width": float(el.get("width")),
                              "svg_height": float(el.get("height"))} for el in images],
        "files": {str((OUT / f"teaser.{ext}").relative_to(ROOT)):
                  digest((OUT / f"teaser.{ext}").read_bytes()) for ext in ("svg", "pdf", "png")},
        "limitations": "The paper directly prints the author-approved three-column layout, including all nine images. At 5.4 inches, vector text is approximately 2.5–4.7 points; small labels remain a readability limitation, not permission to redesign the figure. All preferences and paths are constructed illustrations.",
    }
    (OUT / "teaser.manifest.json").write_text(json.dumps(info, indent=2) + "\n")
    print("Teaser: green method palette; text, geometry and nine embedded images preserved.")


if __name__ == "__main__":
    main()
