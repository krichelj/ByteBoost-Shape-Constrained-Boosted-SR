.PHONY: pdf clean

MAIN = byteboost_project_description

pdf: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex byteboost_refs.bib
	pdflatex -interaction=nonstopmode $(MAIN)
	bibtex $(MAIN)
	pdflatex -interaction=nonstopmode $(MAIN)
	pdflatex -interaction=nonstopmode $(MAIN)

clean:
	rm -f $(MAIN).aux $(MAIN).bbl $(MAIN).blg $(MAIN).log $(MAIN).out
