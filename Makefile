all: shell

help:
	@echo "flask-boilerplate 0.0.4"
	@echo ""
	@echo "Usage"
	@echo "  help		Show this message."
	@echo "  shell		Spawns a shell within the virtual environment."
	@echo "  dev		Local run development server."
	@echo "  prod		Local run production server."
	@echo "  test		Local run testing server."
	@echo "  install	Install the project dependencies."
	@echo "  cli		Run CLI Commands."
	@echo "  lint		Lint all python files."

shell:
	poetry shell

dev:
	FLASK_APP=app FLASK_ENV=development flask run

prod:
	FLASK_APP=app FLASK_ENV=production flask run

test:
	FLASK_APP=app FLASK_ENV=testing flask run

install:
	poetry install

cli:
	FLASK_APP=commands flask $(command)

lint:
	autopep8 -i -v -r `find ./ -name '*.py'`
