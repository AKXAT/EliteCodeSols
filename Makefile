VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip3

run: $(VENV)/bin/activate
	pre-commit install

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

run-tests:
	python3 -m pytest

clean:
	rm -rf __pycache__
	rm -rf Tests/__pycache__
	rm -rf Tests/artifacts/artifacts.log
	rm -rf Tests/results/output.json
	rm -rf Tests/results/results.html
	rm -rf $(VENV)