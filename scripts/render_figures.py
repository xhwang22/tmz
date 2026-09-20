#!/usr/bin/env python3
"""Build isolated vector figures and a visual-review contact sheet (offline)."""

import argparse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import subprocess

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
FIGURES = (
    "teaser", "overview", "c1_landscape", "evaluator", "budget_tests", "simulated_landscape",
    "simulated_alignment", "simulated_acquisition", "simulated_annotation",
    "simulated_selection", "simulated_ablation", "simulated_refinement", "simulated_cost",
)


def render(name, out):
    tex = out / f"{name}.tex"
    tex.write_text(
        "\\documentclass[border=4pt]{standalone}\n\\usepackage{times}\n"
        "\\input{preamble.tex}\n\\begin{document}\n"
        f"\\input{{figures/{name}.tex}}\n\\end{{document}}\n",
        encoding="utf-8",
    )
    result = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
         "-file-line-error", f"-output-directory={out}", str(tex)],
        cwd=ROOT, capture_output=True, text=True,
    )
    (out / f"{name}.build.log").write_text(result.stdout + result.stderr)
    if result.returncode:
        raise RuntimeError(f"{name}:\n{result.stdout[-3500:]}")
    subprocess.run(
        ["pdftoppm", "-singlefile", "-r", "220", "-png",
         str(out / f"{name}.pdf"), str(out / name)], check=True,
        cwd=ROOT, capture_output=True,
    )
    return out / f"{name}.png"


def contact_sheet(paths, destination):
    width, height, pad, header = 1100, 740, 24, 42
    sheet = Image.new("RGB", (2 * width + 3 * pad,
                              ((len(paths) + 1) // 2) * (height + pad) + pad),
                      "#e8edf1")
    draw = ImageDraw.Draw(sheet)
    font_path = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    font = ImageFont.truetype(str(font_path), 22) if font_path.exists() else ImageFont.load_default()
    for index, path in enumerate(paths):
        x = pad + (index % 2) * (width + pad)
        y = pad + (index // 2) * (height + pad)
        draw.rectangle((x, y, x + width, y + height), fill="white")
        number = FIGURES.index(path.stem) + 1
        draw.text((x + 16, y + 10), f"{number:02d}  {path.stem.replace('_', ' ')}",
                  fill="#202c3b", font=font)
        with Image.open(path) as source:
            preview = source.convert("RGB")
            preview.thumbnail((width - 24, height - header - 16), Image.Resampling.LANCZOS)
            sheet.paste(preview, (x + (width - preview.width) // 2,
                                 y + header + (height - header - preview.height) // 2))
    sheet.save(destination)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("names", nargs="*", help="Figure stems; default: all manuscript figures")
    parser.add_argument("--out", default="build/figure-review")
    args = parser.parse_args()
    names = args.names or list(FIGURES)
    if invalid := set(names) - set(FIGURES):
        parser.error(f"Unknown figures: {', '.join(sorted(invalid))}")
    out = (ROOT / args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(max_workers=4) as executor:
        paths = list(executor.map(lambda name: render(name, out), names))
    contact_sheet(paths, out / "contact-sheet.png")
    print(f"Rendered {len(paths)} figures: {out}")


if __name__ == "__main__":
    main()
