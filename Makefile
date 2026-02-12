PYTHON := .venv/bin/python

.PHONY: bootstrap lint format-check typecheck test check-all pre-commit

bootstrap:
	python -m pip install -e ".[dev]"

lint:
	$(PYTHON) -m ruff check .

format-check:
	$(PYTHON) -m ruff format --check .

typecheck:
	$(PYTHON) -m mypy src tests

test:
	$(PYTHON) -m pytest

check-all: lint format-check typecheck test

pre-commit:
	.venv/bin/pre-commit run --all-files
