#!/usr/bin/env python3
"""Update two display labels in the frozen landscape PDF without redrawing it.

Requires PyMuPDF. Pass the pre-IterEval PDF as --source. Its editable SVG has
legacy font metadata that differs from the published PDF, so SVG reconversion
would change typography. This utility retains the PDF's other text and graphics,
uses the same Source Sans fonts for the two replacements, and checks that every
drawing path is unchanged. It never reads or writes numerical fixtures.
"""
import argparse
from collections import Counter
from pathlib import Path

import pymupdf


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    target = root / "figures/simulated/landscape_outcomes.pdf"
    if args.source.resolve() == target:
        parser.error("Keep the original source separate from the output.")
    doc = pymupdf.open(args.source)
    assert len(doc) == 1
    page = doc[0]
    drawings = page.get_drawings()
    old_text = page.get_text()
    spans = [s for b in page.get_text("dict")["blocks"] if "lines" in b
             for line in b["lines"] for s in line["spans"] if "ERA" in s["text"]]
    assert len(spans) == 2 and {s["text"] for s in spans} == {
        "ERA", "Static judge · Static tools · Prompt opt. · Program search · ERA"}
    for span in spans:
        page.add_redact_annot(pymupdf.Rect(span["bbox"]), fill=False)
    page.apply_redactions(images=0, graphics=0)
    for index, span in enumerate(spans):
        text = span["text"].replace("ERA", "IterEval")
        fontfile = root / "build/figure-fonts" / (span["font"] + ".ttf")
        font = pymupdf.Font(fontfile=str(fontfile))
        name = "IterEvalLabel" + str(index)
        page.insert_font(fontname=name, fontfile=str(fontfile))
        x, y = span["origin"]
        if span["text"] == "ERA":
            x = span["bbox"][2] - font.text_length(text, fontsize=span["size"])
        color = tuple(((span["color"] >> shift) & 255) / 255 for shift in (16, 8, 0))
        page.insert_text((x, y), text, fontname=name, fontsize=span["size"], color=color)
    # Sequence numbers change after text replacement; geometry must not.
    geometry = lambda paths: [{k: v for k, v in p.items() if k != "seqno"} for p in paths]
    assert geometry(drawings) == geometry(page.get_drawings())
    new_text = page.get_text()
    assert "ERA" not in new_text and "IterEval" in new_text
    expected = Counter(old_text.replace("ERA", "IterEval").split())
    actual = Counter(new_text.split())
    assert expected == actual, (expected - actual, actual - expected)
    doc.subset_fonts()
    doc.save(target, garbage=4, deflate=True)
    page.get_pixmap(dpi=300).save(target.with_suffix(".png"))
    print("Updated two labels; all other text and all vector drawing paths preserved.")


if __name__ == "__main__":
    main()
