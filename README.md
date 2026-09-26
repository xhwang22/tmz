# EvalOpt

**EvalOpt: Evolving Evaluators for Open-Ended Tasks with Human Feedback**

The Git-tracked package contains the files needed to compile the manuscript,
plus this README and `.gitignore`. The local workspace also contains editable
figure sources, experiment configurations, and research records.

## Compile in Overleaf

Import this repository (or upload its ZIP), then select:

- **Main document:** `main.tex`
- **Compiler:** pdfLaTeX
- **TeX Live:** 2025 or newer

Overleaf runs BibTeX automatically. All figure PDFs and generated table/number
TeX files are included; no Python, external assets, API access, or shell escape
is needed.

For a local TeX Live installation:

```sh
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Draft status

Quantitative displays currently use simulated data; empirical evaluation is
pending. Existing manuscript disclosures are preserved.

Editing scripts, figure sources, experiment plans, and historical assets are
not part of the Overleaf package. The last complete development snapshot is
[commit 62cc2b9](https://github.com/xhwang22/tmz/tree/62cc2b9d1022186af41e15e2c7289c46835a25b8).
When adding a new compilation dependency, also add its path to `.gitignore`'s
allowlist.

## Local workspace

| Location | Role |
| --- | --- |
| `sections/`, `main.tex`, `preamble.tex`, `references.bib` | Current manuscript sources |
| `figures/` | Paper figures, generated tables, editable sources, and provenance manifests |
| `output/fig1-branch-evaluator/` | Current Fig1 SVG, PDF, PNG, and manifest; paper copy: `figures/teaser.pdf` |
| `output/fig1-editable/` | Editable Fig1 PowerPoint, reference image, fonts, and handoff ZIP |
| `figures/overview-selected.svg` | Author-selected editable Fig2; exports: `output/fig2-svg/` |
| `data/` | Experiment configurations, fixtures, templates, and provenance; preserved independently of paper inclusion |
| `scripts/` | Retained rendering, validation, and source-audit utilities |
| `.paper/` | Claim/figure memory, research audits, source records, and revision history |
| `build/` | Current TeX build, retained literature/citation evidence, and offline fonts |

Use `make` to compile locally and `make check` to run the checks. Figure
regeneration is explicit: `scripts/render_overview_selected.py` exports the
selected Fig2 SVG; `scripts/select_branch_teaser.py` publishes the selected
Fig1 exports; `scripts/export_fig1_pptx.py` rebuilds its editable handoff.
These commands write exports; they are not needed for normal paper compilation.

The old `figures` and `palettes` Makefile targets belonged to retired design
studies and have been removed. `make clean` removes TeX intermediates and Python
bytecode, not the literature evidence or fonts stored under `build/`.

The 2026-09-26 cleanup removed unselected visual studies, obsolete preview
scripts, superseded working notes, and intermediate screenshots/logs. A
per-file decision inventory and SHA-256-verified recovery archive are stored
outside the project in `../tmz-cleanup-20260926/`. See
`.paper/project_cleanup_20260926.md` for the audit and validation summary.
