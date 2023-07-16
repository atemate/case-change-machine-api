FROM python:3.10-slim
WORKDIR /workdir

COPY src src
RUN pip install --no-cache-dir ./src/chg-service

CMD ["uvicorn", "change_machine_service.api:app", "--host=0.0.0.0", "--port=3003"]
