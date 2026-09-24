# IterEval

**Dive Deeper, Branch Later: Self-Evolving Evaluators across Open-Ended Tasks**

This branch contains only the files needed to compile the manuscript,
plus this README and `.gitignore`.

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
