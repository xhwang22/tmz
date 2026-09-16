SHELL := /bin/bash
TEXFLAGS := -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build
INPUTS := Makefile main.tex preamble.tex references.bib iclr2027_conference.sty iclr2027_conference.bst $(wildcard sections/*.tex figures/*.tex output/imagegen/*.png)

.PHONY: all check clean
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
	git diff --check

clean:
	rm -rf build
