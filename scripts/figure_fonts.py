"""Shared Palatino-compatible typography for the current manuscript figures.

TeX Gyre Pagella is the freely available Palatino/Palladio derivative shipped
with TeX Live. Resolve real font files and fail instead of silently substituting.
Historical figure renderers intentionally keep their original typography.
"""
from functools import lru_cache
from pathlib import Path
import subprocess

FAMILY = "TeX Gyre Pagella"
SVG_FAMILY = "TeX Gyre Pagella, Palatino, Palatino Linotype, serif"


@lru_cache(maxsize=None)
def font_path(style="regular"):
    name = "texgyrepagella-{}.otf".format(style)
    resolved = subprocess.check_output(["kpsewhich", name], text=True).strip()
    path = Path(resolved)
    if not resolved or not path.is_file():
        raise RuntimeError("Install TeX Gyre Pagella (TeX Live tex-gyre): " + name)
    return path


def configure():
    import matplotlib.pyplot as plt
    from matplotlib.font_manager import FontProperties, fontManager

    paths = {style: font_path(style) for style in ("regular", "bold", "italic", "bolditalic")}
    for path in paths.values():
        fontManager.addfont(str(path))
    plt.rcParams.update({
        "font.family": FAMILY, "pdf.fonttype": 42, "ps.fonttype": 42,
        "svg.fonttype": "none", "svg.hashsalt": "itereval-palatino",
        "axes.unicode_minus": True, "mathtext.fontset": "custom",
        "mathtext.rm": FAMILY, "mathtext.it": FAMILY + ":italic",
        "mathtext.bf": FAMILY + ":bold", "mathtext.sf": FAMILY,
    })
    return {role: FontProperties(fname=str(paths[style])) for role, style in
            (("body", "regular"), ("strong", "bold"), ("serif", "regular"), ("italic", "italic"))}
