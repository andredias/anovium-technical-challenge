SHELL := /usr/bin/env bash -O globstar


test:
	pytest -x --cov-report term-missing --cov-report html --cov-branch \
	       --cov anovium/


lint:
	@echo
	ruff .
	@echo
	blue --check --diff --color .
	@echo
	mypy .
	@echo
	pip-audit


format:
	ruff --silent --exit-zero --fix .
	blue .
