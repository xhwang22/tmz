# EvalOpt

**Evolving Evaluators for Open-Ended Tasks with Human Feedback**

This repository contains the ICLR 2027 manuscript source and its compiled PDF.
The paper studies how feedback from people can be used to evolve executable
evaluation programs for open-ended generation tasks.

## Read the paper

The latest compiled manuscript is available as [`paper.pdf`](paper.pdf).

## Build

The manuscript requires GNU Make and a TeX Live installation containing
`pdflatex` and `bibtex`.

```bash
make clean && make
```

The build writes intermediate files to `build/` and copies the resulting PDF to
`paper.pdf`. The entry point is `main.tex`.

## Repository layout

- `sections/`: manuscript sections and appendix
- `figures/`: LaTeX figure sources and rendered figure assets
- `references.bib`: bibliography
- `iclr2027_conference.sty` and `iclr2027_conference.bst`: conference style

## Scope

This is a manuscript repository, not the complete experiment artifact. It does
not include the full training/evaluation implementation, model-service
configuration, or raw experiment records. The paper and appendix document the
method, aggregate results, and evaluation protocols available in this bundle.
