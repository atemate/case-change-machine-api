install:
	poetry install --with=dev

lint:
	poetry run pre-commit run -a

unit-tests:
	poetry run pytest -sv ./src
