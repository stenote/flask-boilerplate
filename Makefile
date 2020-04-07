all: web

help:
	@echo "flask-boilerplate 0.0.1"
	@echo ""
	@echo "Usage"
	@echo "  help		Show this message."
	@echo "  shell		Spawns a shell within the virtual environment."
	@echo "  web    	Local run dev server."
	@echo "  env		Installs the project dependencies."
	@echo "  cli	    	Run CLI Commands."
	@echo "  lint		Lint all python files."

shell:
	poetry shell

web:
	poetry shell && FLASK_APP=app FLASK_ENVIRONMENT=development FLASK_DEBUG=True flask run

env:
	poetry install

cli:
	poetry shell && FLASK_APP=commands flask $(COMMAND)

lint:
	poetry shell && autopep8 -i -v -r `find ./ -name '*.py'`
