.PHONY: pdf clean

DOC_DIR = documents/description
MAIN = byteboost_project_description

pdf: $(DOC_DIR)/$(MAIN).pdf

$(DOC_DIR)/$(MAIN).pdf: $(DOC_DIR)/$(MAIN).tex $(DOC_DIR)/byteboost_refs.bib
	cd $(DOC_DIR) && pdflatex -interaction=nonstopmode $(MAIN)
	cd $(DOC_DIR) && bibtex $(MAIN)
	cd $(DOC_DIR) && pdflatex -interaction=nonstopmode $(MAIN)
	cd $(DOC_DIR) && pdflatex -interaction=nonstopmode $(MAIN)

clean:
	cd $(DOC_DIR) && rm -f $(MAIN).aux $(MAIN).bbl $(MAIN).blg $(MAIN).log $(MAIN).out
