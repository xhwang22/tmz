SHELL := /bin/bash
.DEFAULT_GOAL := all
.DELETE_ON_ERROR:

PDFLATEX ?= pdflatex
BIBTEX ?= bibtex
TEXFLAGS := -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape -recorder -output-directory=build
INPUTS := Makefile main.tex preamble.tex references.bib iclr2027_conference.sty iclr2027_conference.bst \
		  $(wildcard sections/*.tex figures/*.tex figures/*.pdf figures/results/*.tex figures/results/*.pdf figures/mining_diagnostics/*.tex figures/mining_diagnostics/*.pdf figures/downstream/*.tex)

.PHONY: all clean
all: paper.pdf

build/main.pdf: $(INPUTS)
	@mkdir -p build
	$(PDFLATEX) $(TEXFLAGS) main.tex
	cd build && BIBINPUTS="../:" BSTINPUTS="../:" $(BIBTEX) main
	$(PDFLATEX) $(TEXFLAGS) main.tex
	$(PDFLATEX) $(TEXFLAGS) main.tex
	$(PDFLATEX) $(TEXFLAGS) main.tex

paper.pdf: build/main.pdf
	cp build/main.pdf paper.pdf

clean:
	rm -f build/main.aux build/main.bbl build/main.blg build/main.fls build/main.log build/main.out build/main.pdf build/main.toc build/main.synctex.gz paper.pdf
