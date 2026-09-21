#!/usr/bin/env python3
"""Export the author-edited v6 teaser and its current local refinements.

The self-contained SVG is the source of truth: do not regenerate it from an
older wording profile. Recoloring preserves the current source text, geometry
and nine embedded images. Surface styling and panel-a conflict annotations are
separate revisions; surface edits preserve semantic groups. No image generation.
"""
import base64
from collections import Counter
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
                           "palette_check": "current source text, geometry and embedded images unchanged by export",
                           "elements": dict(Counter(el.tag.split('}')[-1] for el in doc.iter()))})
    reflowed = doc.get("data-layout") == "shared-case-above-symmetric-method-panels"
    typography_polished = doc.get("data-polish") in {"strong-type-short-labels", "compact-flat-hierarchy"}
    if reflowed:
        asset_manifest["surface_polish"] = {
            "date": "2026-09-21", "reference": "figures/overview.png",
            "changes": ["flat peach/blue/green panels", "white revision cards with plain mint headers",
                        "stronger action headings, shorter diagnostics and heavier active paths",
                        "compact shared case strip and one flat surface grouping the default checks"],
            "scope": "rejected gradient, fold and stacked-edge pass removed",
        }
        asset_manifest["layout_revision"] = {
            "layout": doc.get("data-layout"),
            "preserved": ["all nine image payloads and original crops",
                          "branch path coordinates, node geometry and attempt order"],
            "changed": ["shared case strip above two equal-width method panels",
                        "uniform group transforms; repositioned task annotations",
                        "authorized label compression, font sizes and stroke weights"],
            "not_changed": ["branch topology", "path coordinates inside groups",
                            "solid/dashed arrow semantics", "case trade-off and local ordering outcomes"],
        }
        asset_manifest["style"] = "flat pale panels and restrained outlines; no gradients, folds or layered shadows"
        asset_manifest["flat_style_check"] = "no linear/radial gradients or filters"
    elif doc.find(".//s:style[@id='surface-polish-style']", NS) is not None:
        asset_manifest["surface_polish"] = {
            "date": "2026-09-21",
            "reference": "figures/overview.png",
            "changes": ["graduated peach/blue/green paper surfaces",
                        "layered default-check cards and stacked revision sheets",
                        "mint header bands, folded corners and crisp paper edges",
                        "photo mounts and shaded node rims"],
            "preserved_at_surface_revision": ["all current labels, including panel-a conflict annotations",
                                              "9 embedded images and their crops",
                                              "all original path coordinates", "panel, card and node positions"],
            "scope": "second surface-only pass; no change to content, layout or search semantics",
        }
        asset_manifest["style"] = "layered paper cards, soft graduated surfaces, photo mounts and graded search nodes"
        asset_manifest["flat_style_check"] = "superseded by author-requested surface styling"
    if doc.find(".//s:g[@id='task-ranking-conflict']", NS) is not None:
        asset_manifest["panel_a_revision"] = {
            "date": "2026-09-21",
            "purpose": "make the criterion trade-off and opposite overall rankings explicit",
            "changes": ["two aligned qualitative comparison rows", "explicit Human: A > B versus Evaluator: B > A"],
            "preserved": ["all nine embedded images and crops", "comparison wording", "pointwise-scoring note"],
            "evidence_status": "constructed illustration; not measured metric scores or collected human preferences",
        }
    (SOURCE.parent / "manifest.json").write_text(json.dumps(asset_manifest, indent=2) + "\n")
    info = {
        "source": str(SOURCE.relative_to(ROOT)), "source_sha256": digest(svg.encode()),
        "author_wording_preserved": not typography_polished, "geometry_preserved": not reflowed,
        "branch_geometry_preserved": True,
        "typography_polish": typography_polished,
        "layout_revision": asset_manifest.get("layout_revision"),
        "preservation_basis": "current editable SVG at export time, not the historical wording profile",
        "method_accent": "#62AAA5", "error_status_colors_preserved": True,
        "empirical_evidence": False, "constructed_illustration": True,
        "new_generation": False, "print_width_in": 5.4,
        "surface_polish": asset_manifest.get("surface_polish"),
        "panel_a_revision": asset_manifest.get("panel_a_revision"),
        "paper_layout": "figures/teaser.tex",
        "paper_graphic": "figures/teaser.pdf",
        "image_source": asset_manifest["source"],
        "image_source_sha256": asset_manifest["source_sha256"],
        "embedded_images": [{"sha256": digest(base64.b64decode(el.get(HREF).split(",", 1)[1])),
                              "svg_width": float(el.get("width")),
                              "svg_height": float(el.get("height"))} for el in images],
        "files": {str((OUT / f"teaser.{ext}").relative_to(ROOT)):
                  digest((OUT / f"teaser.{ext}").read_bytes()) for ext in ("svg", "pdf", "png")},
        "limitations": "All nine original images/crops and both search-tree geometries are retained. Labels are shortened and enlarged, with thicker active paths on flat surfaces. Some vector labels remain below 7 points at 5.4-inch print width. All preferences and paths are constructed illustrations.",
    }
    (OUT / "teaser.manifest.json").write_text(json.dumps(info, indent=2) + "\n")
    print("Teaser exported: current SVG content and all nine images preserved; panel-a conflict annotations included.")


if __name__ == "__main__":
    main()
