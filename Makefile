
.PHONY: all local-run venv run-commands

all: local-run

local-run:
	source ./venv/bin/activate && FLASK_APP=app FLASK_ENVIRONMENT=development FLASK_DEBUG=True flask run

venv:
	rm -rf ./venv
	python3 -m venv venv && source ./venv/bin/activate && pip install -r requirements.txt

run-commands:
	source ./venv/bin/activate && FLASK_APP=commands flask

