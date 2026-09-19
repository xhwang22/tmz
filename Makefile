SHELL := /bin/bash
TEXFLAGS := -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build
INPUTS := Makefile main.tex preamble.tex references.bib iclr2027_conference.sty iclr2027_conference.bst $(wildcard sections/*.tex figures/*.tex figures/simulated/*.tex figures/simulated/*.pdf output/imagegen/*.png)

.PHONY: all check figures simulated palettes clean
all: paper.pdf

build/main.pdf: $(INPUTS)
	mkdir -p build
	pdflatex $(TEXFLAGS) main.tex
	cd build && BIBINPUTS="../:" BSTINPUTS="../:" bibtex main
	pdflatex $(TEXFLAGS) main.tex
	pdflatex $(TEXFLAGS) main.tex
	pdflatex $(TEXFLAGS) main.tex

paper.pdf: build/main.pdf
	cp build/main.pdf paper.pdf

check: paper.pdf
	python3 scripts/check_paper.py
	python3 scripts/check_memory.py
	python3 scripts/check_simulated_results.py
	python3 scripts/check_landscape_results.py
	git diff --check

# Optional regeneration; committed vector assets keep normal compilation offline.
simulated:
	python3 scripts/render_simulated_results.py

# Optional visual review: requires Pillow, standalone.cls, and pdftoppm.
figures:
	python3 scripts/render_figures.py

# Three author-reference palettes on identical fixtures, charts, and diagrams.
palettes:
	python3 scripts/render_palette_candidates.py

clean:
	rm -rf build
