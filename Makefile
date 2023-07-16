install:
	poetry install --with=dev

lint:
	poetry run pre-commit run -a

unit-tests:
	poetry run pytest -sv ./src

run-local:
	poetry run uvicorn change_machine_service.api:app --reload

run-docker:
	docker-compose -f ./docker-compose.yaml up --build chg_service

stop-docker:
	docker-compose down --remove-orphans


# disable make caching:
.PHONY: install lint unit-tests run-docker run-local stop-docker
