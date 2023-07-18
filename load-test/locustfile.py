import logging
import random

from locust import HttpUser, between, task


def _get_random_2digit_float(n_max: int):
    return float("{:.2f}".format(random.random() * n_max))


class QuickstartUser(HttpUser):
    # host = f"http://{SERVER_HOST}:{SERVER_PORT}"
    wait_time = between(0.001, 1)

    @task
    def get_pay(self):
        input = _get_random_2digit_float(10000)
        price = _get_random_2digit_float(10)
        query = f"/pay?eur_inserted={input}&currywurst_price_eur={price}"
        logging.info(f"GET {query}")
        self.client.get(query)
