.PHONY: run install clean check runner
.DEFAULT_GOAL := runner

run: install
	cd rent_prediction; poetry run python3 runner.py

install: pyproject.toml
	poetry install

clean:
	rm -rf `find . -type d -name __pycache__`

check:
	poetry run flake8 rent_prediction

format:
	poetry run black rent_prediction

runner: format check run clean

