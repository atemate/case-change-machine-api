import logging
import random

from locust import HttpUser, between, task


def _get_random_2digit_float(n_max: int):
    return float("{:.2f}".format(random.random() * n_max))


class QuickstartUser(HttpUser):
    wait_time = between(0.0001, 0.1)

    @task
    def get_pay(self):
        input = _get_random_2digit_float(1000)
        price = _get_random_2digit_float(25)
        query = f"/pay?eur_inserted={input}&currywurst_price_eur={price}"
        logging.info(f"GET {query}")
        self.client.get(query)
