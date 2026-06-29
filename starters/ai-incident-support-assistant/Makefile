# AI Incident Support Assistant — starter Makefile
# Unix / macOS / Linux. Standard library only. No LLM, no network, no Docker.

PYTHON ?= python3

.PHONY: help setup test check inspect-dataset manual-baseline evidence

help:
	@echo "Available commands:"
	@echo "  make setup           - check your Python install and print next steps"
	@echo "  make test            - validate the synthetic dataset"
	@echo "  make check           - run the test and confirm success"
	@echo "  make inspect-dataset - print a read-only summary of the dataset (Lab 02)"
	@echo "  make manual-baseline - run a weak, rule-based baseline (NOT AI) (Lab 02)"
	@echo "  make evidence        - check minimum Level 1 evidence files (no AI, read-only)"
	@echo "  make help            - show this help"

setup:
	@echo "== AI Incident Support Assistant — setup =="
	@if command -v python3 >/dev/null 2>&1; then \
		echo "Found python3: $$(python3 --version 2>&1)"; \
	elif command -v python >/dev/null 2>&1; then \
		echo "Found python: $$(python --version 2>&1)"; \
	else \
		echo "ERROR: Python 3 was not found. Install it from https://www.python.org/"; \
		exit 1; \
	fi
	@echo "No dependencies to install: this starter uses only the Python standard library."
	@echo "Next: run 'make test' to validate the synthetic dataset, then 'make check'."

test:
	@if command -v python3 >/dev/null 2>&1; then \
		python3 tests/test_dataset.py && python3 tests/test_check_evidence.py; \
	else \
		python tests/test_dataset.py && python tests/test_check_evidence.py; \
	fi

check: test
	@echo "CHECK PASSED: the synthetic dataset is valid. You are ready for Level 1."

inspect-dataset:
	@$(PYTHON) scripts/inspect_dataset.py

manual-baseline:
	@$(PYTHON) scripts/manual_baseline.py

evidence:
	@$(PYTHON) scripts/check_evidence.py
