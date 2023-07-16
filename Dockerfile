FROM python:3.10-slim
WORKDIR /workdir

COPY src src
RUN pip install --no-cache-dir ./src/chg-service

CMD ["python", "-m", "change_machine_service.api"]
