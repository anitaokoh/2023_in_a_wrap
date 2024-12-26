install_poetry:
	curl -sSL https://install.python-poetry.org | python -

install_dependencies:
	poetry install

test:
	poetry run pytest -vv --cov=tests --ignore=tests/test_emotion_analyzer.py

requirement_file:
	poetry export -f requirements.txt --output requirements.txt
