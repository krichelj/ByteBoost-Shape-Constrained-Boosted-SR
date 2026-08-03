.PHONY: pdf clean all check description

pdf all description:
	bash scripts/compile.sh description

clean:
	bash scripts/compile.sh clean

# From-scratch quality gate (errors + warnings).
check:
	bash scripts/check-latex.sh
