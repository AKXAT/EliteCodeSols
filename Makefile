VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip3

run: $(VENV)/bin/activate
	pre-commit install

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt


clean:
	rm -rf __pycache__
	rm -rf *.log
	rm -rf *.xml
	rm -rf $(VENV)