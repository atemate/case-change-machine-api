install:
	poetry install --with=dev

lint:
	poetry run pre-commit run -a

unit-tests:
	poetry run pytest -sv ./src

run-local:
	poetry run uvicorn change_machine_service.api:app --reload

run-docker:
	docker-compose -f ./docker-compose-single.yaml up --build

stop-docker:
	docker-compose -f ./docker-compose-single.yaml down --remove-orphans


run-docker-elk:
	docker-compose -f docker-compose-elk.yaml up --build

open-kibana:
	open http://localhost:5601/app/management/kibana/indexPatterns

stop-docker-elk:
	docker-compose -f docker-compose-elk.yaml down  --remove-orphans


# disable make caching:
.PHONY: install lint unit-tests run-docker run-local stop-docker run-complex-docker
