install_poetry:
	curl -sSL https://install.python-poetry.org | python -

install_dependencies:
	poetry install

test:
	poetry run pytest -vv --cov=tests

requirement_file:
	poetry export -f requirements.txt --output requirements.txt
