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

cleanup-docker:
	docker-compose -f ./docker-compose-single.yaml down --remove-orphans -v


run-docker-elk:
	docker-compose -f docker-compose-elk.yaml up --build

cleanup-docker-elk:
	docker-compose -f docker-compose-elk.yaml down --remove-orphans -v


open-kibana:
	open http://localhost:5601/app/dashboards

setup-kibana:
	KIBANA_URL=http://localhost:5601 \
	DATA_VIEW_CONFIG_NDJSON=docker/kibana/coins-dashboard.ndjson \
	sh ./docker/kibana/curl-create-dashboard.sh


run-load-test:
	docker-compose -f docker-compose-locust.yaml up --scale locust_worker=2

cleanup-load-test:
	docker-compose -f docker-compose-locust.yaml down --remove-orphans -v


# disable make caching:
.PHONY: install lint unit-tests run-local run-docker cleanup-docker run-docker-elk cleanup-docker-elk open-kibana setup-kibana run-load-test cleanup-load-test
