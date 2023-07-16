install:
	poetry install --with=dev

lint:
	poetry run pre-commit run -a

unit-tests:
	poetry run pytest -sv ./src

run-local:
	poetry run uvicorn change_machine_service.api:app --reload

run-docker:
	docker-compose -f ./docker-compose-single.yaml up

stop-docker:
	docker-compose -f ./docker-compose-single.yaml down --remove-orphans


run-complex-docker:
	rm -rf ./logs
	mkdir -p ./logs/kafka-data
	mkdir -p ./logs/zk-data
	mkdir -p ./logs/zk-txn-logs
	mkdir -p ./logs/postgres-data
	mkdir -p ./logs/pgadmin
	mkdir -p ./logs/grafana-data/data
	mkdir -p ./logs/grafana-data/certs
	docker-compose -f ./docker-compose-complex.yaml up


# disable make caching:
.PHONY: install lint unit-tests run-docker run-local stop-docker run-complex-docker
