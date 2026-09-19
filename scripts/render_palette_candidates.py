#!/usr/bin/env python3
"""Compare the author's three reference palettes on identical native figures.

Labeled HEX swatches are the source of color, not JPEG pixel estimates. Original
reference thumbnails appear only in local build/ proofs, never the manuscript.
All values are disclosed simulations; palette review cannot change the fixtures.
"""

from concurrent.futures import ThreadPoolExecutor
import csv
import hashlib
import json
import math
import re
import subprocess
import sys

from matplotlib import font_manager
from PIL import Image, ImageDraw, ImageFont, ImageOps

from render_simulated_results import (DEFAULT_PALETTE, DISPLAY_METHODS, ON_FILL, PALETTES, ROOT,
                                      TEX_ROLES, contrast, on_fill, tint)

OUT = ROOT / "build/reference-palettes"
ROLES = (("BLUE", "Static judge"), ("MINT", "Static tools"), ("CREAM", "Prompt opt."),
         ("PEACH", "Program search"), ("ROSE", "ERA"))
WASHES = {"pBlueWash": ("pSky", 17), "pTealWash": ("pMint", 28),
          "pGoldWash": ("pCream", 38), "pResearchWash": ("pLilac", 16),
          "pEvoWash": ("pRose", 10), "pRedWash": ("pRose", 13)}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def font(size, bold=False):
    path = font_manager.findfont(font_manager.FontProperties(
        family="TeX Gyre Heros", weight="bold" if bold else "normal"))
    return ImageFont.truetype(path, size)


def diagram(name, destination, colors):
    overrides = [f"\\definecolor{{{role}}}{{HTML}}{{{colors[key][1:]}}}"
                 for role, key in TEX_ROLES.items()]
    overrides += [f"\\colorlet{{{role}}}{{{base}!{amount}!white}}"
                  for role, (base, amount) in WASHES.items()]
    overrides += [r"\colorlet{pCoral}{pRose}", r"\colorlet{pPaper}{white}"]
    tex = destination / f"{name}.tex"
    tex.write_text("\\documentclass[border=4pt]{standalone}\n\\usepackage{times}\n"
                   "\\input{preamble.tex}\n" + "\n".join(overrides)
                   + f"\n\\begin{{document}}\n\\input{{figures/{name}.tex}}\n\\end{{document}}\n",
                   encoding="utf-8")
    result = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                             "-file-line-error", f"-output-directory={destination}", str(tex)],
                            cwd=ROOT, capture_output=True, text=True)
    (destination / f"{name}.build.log").write_text(result.stdout + result.stderr)
    if result.returncode:
        raise RuntimeError(result.stdout[-3500:] + result.stderr)
    subprocess.run(["pdftoppm", "-singlefile", "-r", "220", "-png",
                    str(destination / f"{name}.pdf"), str(destination / name)],
                   cwd=ROOT, capture_output=True, check=True)


def render(name):
    destination = OUT / name
    result = subprocess.run([sys.executable, str(ROOT / "scripts/render_simulated_results.py"),
                             "--palette", name, "--preview-root", str(destination)],
                            cwd=ROOT, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stdout + result.stderr)
    canonical = sorted((ROOT / "data/simulated").glob("*.csv"))
    matches = {p.name: digest(p) == digest(destination / "data" / p.name) for p in canonical}
    matches["c1_table.tex"] = digest(ROOT / "figures/simulated/c1_table.tex") == digest(destination / "pdf/c1_table.tex")
    if len(canonical) != 14 or not all(matches.values()):
        raise ValueError(f"{name}: candidate changed the fixture data: {matches}")
    colors = PALETTES[name]
    exact = {role: colors[role] == colors["source_swatches"][index]
             for role, index in colors["source_indices"].items()}
    if not all(exact.values()):
        raise ValueError(f"{name}: a fill no longer matches its labeled reference swatch")
    if len({colors[key] for key, _ in ROLES}) != 5:
        raise ValueError(f"{name}: the five-series palette must contain five distinct source colors")
    # Every domain/method cell and paired interval is checked independently.
    displayed = json.loads((destination / "png/outcomes-summary.json").read_text())
    with (destination / "data/c1_summary.csv").open(newline="") as source:
        summary_rows = list(csv.DictReader(source))
    with (destination / "data/alignment_effects.csv").open(newline="") as source:
        effect_rows = list(csv.DictReader(source))
    expected_domains = {f"TD-{family}{i}" for family, count in (("SV", 6), ("IG", 6), ("TG", 5), ("AR", 5))
                        for i in range(1, count+1)}
    if (displayed["methods"] != list(DISPLAY_METHODS)
            or set(displayed["domains"]) != expected_domains
            or len(displayed["method_values"]) != 110
            or len(displayed["paired_effects"]) != 22):
        raise ValueError(f"{name}: main figure omitted a domain, method, or paired effect")
    value_matches = {}
    for item in displayed["method_values"]:
        source = [row for row in summary_rows if row["metric"] == "pairwise"
                  and all(row[key] == item[key] for key in ("domain", "setting", "method", "split"))]
        key = "/".join(item[field] for field in ("domain", "method", "split"))
        value_matches[key] = len(source) == 1 and math.isclose(
            item["agreement_pct"], 100 * float(source[0]["mean"]), abs_tol=1e-10)
    effect_matches = {}
    for item in displayed["paired_effects"]:
        source = [row for row in effect_rows if row["domain"] == item["domain"] and row["split"] == item["split"]]
        effect_matches[item["domain"]] = len(source) == 1 and all(
            math.isclose(float(source[0][key]), item[key], abs_tol=1e-10)
            for key in ("delta_pp", "lower", "upper", "complete_pairs"))
    if len(value_matches) != 110 or not all(value_matches.values()) or not all(effect_matches.values()):
        raise ValueError(f"{name}: displayed C1 cells or paired intervals differ from their source data")
    ratios = {f"{key}/white": contrast(colors[key], "#FFFFFF")
              for key in ("INK", "MUTED", "RED", "GREEN", "BROWN", "BLUE_INK", "GOLD_INK")}
    ratios.update({f"label/{key}": contrast(on_fill(colors[key]), colors[key]) for key, _ in ROLES})
    ratios.update({"badge": contrast(colors["RED"], tint(colors["ROSE"]))})
    ratios.update({f"heatmap/{key}": contrast(ON_FILL, colors[key]) for key, _ in ROLES})
    for role, (base, amount) in WASHES.items():
        background = tint(colors[TEX_ROLES[base]], amount / 100)
        ratios[f"muted/{role}"] = contrast(colors["MUTED"], background)
    for ink, base, amount in (("BLUE_INK", "SKY", .17), ("GREEN", "MINT", .28),
                              ("GOLD_INK", "CREAM", .38), ("RESEARCH", "LILAC", .16),
                              ("RED", "ROSE", .10)):
        ratios[f"diagram/{ink}"] = contrast(colors[ink], tint(colors[base], amount))
    if min(ratios.values()) < 4.5:
        raise ValueError(f"{name}: insufficient small-text contrast: {ratios}")
    diagram("overview", destination, colors)
    subprocess.run(["pdfunite", str(destination / "pdf/outcomes.pdf"),
                    str(destination / "pdf/ablation.pdf"), str(destination / "main-figures.pdf")], check=True)
    for stem in ("outcomes", "ablation"):
        with Image.open(destination / "png" / f"{stem}.png") as source:
            ImageOps.grayscale(source).save(destination / f"{stem}-grayscale.png")
    source = ROOT / colors["source"]
    return {"palette": name, "title": colors["title"], "source": colors["source"],
            "source_image_sha256": digest(source) if source.is_file() else None,
            "color_source": "HEX values printed beneath the author-supplied swatches",
            "reference_swatches": colors["source_swatches"], "exact_source_fills": exact,
            "role_colors": {label: colors[role] for role, label in ROLES},
            "full_five_color_series": True, "main_figure_domain_value_checks": value_matches,
            "main_figure_paired_effect_checks": effect_matches,
            "same_numbers": matches,
            "text_contrast": {key: round(value, 3) for key, value in ratios.items()},
            "simulation_only": True, "is_provisional_manuscript_palette": name == DEFAULT_PALETTE}


def swatches(draw, colors, x, y, width):
    gap = 14
    cell = (width - 4 * gap) // 5
    for index, (role, label) in enumerate(ROLES):
        left = x + index * (cell + gap)
        draw.rounded_rectangle((left, y, left + cell, y + 34), radius=4, fill=colors[role])
        draw.text((left, y + 43), label, font=font(21), fill=colors["INK"])
        draw.text((left, y + 72), colors[role], font=font(20), fill=colors["MUTED"])


def paste_chart(canvas, path, x, y, width):
    with Image.open(path) as source:
        chart = source.convert("RGB")
        height = round(chart.height * width / chart.width)
        chart = chart.resize((width, height), Image.Resampling.LANCZOS)
        canvas.paste(chart, (x, y))
    return height


def comparison():
    # Same-size figures, white paper, no decorative color blocks around the data.
    pad, width, masthead = 32, 1188, 140
    height = 252 + 2 * 20 + 85
    for stem in ("outcomes", "ablation"):
        with Image.open(OUT / DEFAULT_PALETTE / "png" / f"{stem}.png") as source:
            height += round(source.height * (width-20) / source.width)
    canvas = Image.new("RGB", (3 * width + 4 * pad, height + 2 * pad + masthead), "#F4F4F4")
    draw = ImageDraw.Draw(canvas)
    draw.text((pad + 8, 24), "Complete palettes, used together.", font=font(46, True), fill="#25272B")
    draw.text((pad + 8, 89), "22-domain atlas + diagnostic detail  /  exact reference swatches  /  identical simulated observations",
              font=font(27), fill="#60656C")
    for index, (name, colors) in enumerate(PALETTES.items()):
        x, y = pad + index * (width + pad), masthead + pad
        draw.rectangle((x, y, x + width, y + height), fill="white")
        draw.text((x + 28, y + 24), f"{chr(65 + index)}  /  {colors['title']}",
                  font=font(34, True), fill=colors["INK"])
        draw.text((x + 28, y + 77), f"Source: {colors['source']}", font=font(24), fill=colors["MUTED"])
        swatches(draw, colors, x + 28, y + 130, width - 56)
        yy = y + 252
        for stem in ("outcomes", "ablation"):
            yy += paste_chart(canvas, OUT / name / "png" / f"{stem}.png", x + 10, yy, width - 20) + 20
        draw.text((x + 28, y + height - 55), "One coordinated five-color set; labels and shapes retain meaning.",
                  font=font(22), fill=colors["MUTED"])
    canvas.save(OUT / "reference-comparison.png")


def spreads():
    for index, (name, colors) in enumerate(PALETTES.items()):
        width, pad, top = 1188, 30, 265
        sources = [OUT / name / "png" / f"{stem}.png" for stem in ("outcomes", "ablation")]
        heights = []
        for path in sources:
            with Image.open(path) as source:
                heights.append(round(source.height * width / source.width))
        canvas = Image.new("RGB", (width + 2 * pad, top + sum(heights) + 3 * pad + 55), "white")
        draw = ImageDraw.Draw(canvas)
        draw.text((pad, 24), f"{chr(65 + index)}  /  {colors['title']}", font=font(37, True), fill=colors["INK"])
        draw.text((pad, 81), f"Exact source palette: {colors['source']}  /  values are simulated",
                  font=font(24), fill=colors["MUTED"])
        swatches(draw, colors, pad, 133, width)
        y = top
        for path in sources:
            y += paste_chart(canvas, path, pad, y, width) + pad
        draw.text((pad, y + 10), "Methods, task families and feedback levels have separate, explicit color encodings.",
                  font=font(22), fill=colors["MUTED"])
        canvas.save(OUT / name / "main-figures.png")


def sources_board():
    # Local attribution proof only: user-owned originals are not copied into
    # tracked output directories, the manuscript, or a remote image service.
    pad, width, height = 32, 800, 1050
    canvas = Image.new("RGB", (3 * width + 4 * pad, height + 2 * pad), "#F4F4F4")
    draw = ImageDraw.Draw(canvas)
    for index, (name, colors) in enumerate(PALETTES.items()):
        x, y = pad + index * (width + pad), pad
        draw.rectangle((x, y, x + width, y + height), fill="white")
        draw.text((x + 24, y + 20), f"{chr(65 + index)}  /  {colors['title']}", font=font(29, True), fill=colors["INK"])
        path = ROOT / colors["source"]
        if path.is_file():
            with Image.open(path) as source:
                preview = source.convert("RGB")
                preview.thumbnail((width - 60, 680), Image.Resampling.LANCZOS)
                canvas.paste(preview, (x + (width-preview.width)//2, y + 80))
        else:
            draw.text((x + 24, y + 110), "Local reference image not present.", font=font(26), fill=colors["MUTED"])
        draw.text((x + 24, y + 785), "Original labeled swatches (not JPEG samples)", font=font(25), fill=colors["INK"])
        count = len(colors["source_swatches"])
        gap = 8
        cell = (width - 48 - (count-1) * gap) / count
        for i, color in enumerate(colors["source_swatches"]):
            left = round(x + 24 + i * (cell + gap))
            draw.rectangle((left, y + 835, left + round(cell), y + 898), fill=color)
            draw.text((left, y + 911), color, font=font(16 if count > 5 else 20), fill=colors["MUTED"])
        draw.text((x + 24, y + 975), colors["source"] + "  /  local author reference", font=font(22), fill=colors["MUTED"])
    canvas.save(OUT / "reference-sources.png")


def overview_comparison():
    pad, width, top = 32, 1188, 90
    paths = [OUT / name / "overview.png" for name in PALETTES]
    with Image.open(paths[0]) as source:
        height = round(source.height * width / source.width)
    canvas = Image.new("RGB", (3 * width + 4 * pad, height + top + 2 * pad), "#F4F4F4")
    draw = ImageDraw.Draw(canvas)
    for index, ((_, colors), path) in enumerate(zip(PALETTES.items(), paths)):
        x = pad + index * (width + pad)
        draw.rectangle((x, pad, x + width, pad + top + height), fill="white")
        draw.text((x + 24, pad + 20), f"{chr(65 + index)}  /  {colors['title']}", font=font(34, True), fill=colors["INK"])
        paste_chart(canvas, path, x, top + pad, width)
    canvas.save(OUT / "overview-comparison.png")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    tex = (ROOT / "preamble.tex").read_text(encoding="utf-8")
    colors = PALETTES[DEFAULT_PALETTE]
    for role, key in TEX_ROLES.items():
        match = re.search(r"\\definecolor\{" + role + r"\}\{HTML\}\{([A-Fa-f0-9]+)\}", tex)
        if match is None or match.group(1).lower() != colors[key][1:].lower():
            raise ValueError(f"The canonical diagram and chart palettes disagree: {role}")
    # Isolated processes keep Matplotlib globals and data copies independent.
    with ThreadPoolExecutor(max_workers=2) as executor:
        reports = list(executor.map(render, PALETTES))
    comparison()
    spreads()
    sources_board()
    overview_comparison()
    report = {"simulation_only": True, "provisional_default": DEFAULT_PALETTE,
              "data_and_layout_identical_across_candidates": True, "candidates": reports}
    (OUT / "review.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Three reference-faithful palettes, main diagrams, vector PDFs and grayscale proofs: {OUT}")
    print("All 14 CSV files and the numerical table match the canonical fixtures byte for byte.")


if __name__ == "__main__":
    main()
