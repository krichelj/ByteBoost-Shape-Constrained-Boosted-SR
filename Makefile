.PHONY: pdf clean abstract all check description

pdf all:
	bash scripts/compile.sh all

description:
	bash scripts/compile.sh description

abstract:
	bash scripts/compile.sh abstract

clean:
	bash scripts/compile.sh clean

# From-scratch quality gate (errors + warnings). Used by CI and pre-push.
check:
	bash scripts/check-latex.sh
