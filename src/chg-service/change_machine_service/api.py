import logging
from typing import Any

import uvicorn
from change_machine_package import return_coins
from fastapi import FastAPI

from .exceptions import register_exception_handlers
from .logger import log
from .settings import SETTINGS

app = FastAPI()
api_v1 = FastAPI()
app.mount(SETTINGS["server"].prefix, api_v1)

register_exception_handlers(app)


@api_v1.get("/health")
def get_health():
    return {}


@api_v1.get("/info")
async def get_info():
    return dict(SETTINGS)


@api_v1.get("/pay")
def get_pay(
    product_price_eur: float,
    eur_inserted: float,
):
    chg_settings = SETTINGS["change_machine"]
    kwargs: dict[str, Any] = dict(
        product_price_eur=product_price_eur,
        eur_inserted=eur_inserted,
        algorithm=chg_settings.algorithm,
        return_coins_only=chg_settings.return_coins_only,
    )
    change = return_coins(**kwargs)
    log.info(
        "Coins calculated",
        extra=dict(**kwargs, change=change),
    )
    return change


if __name__ == "__main__":
    srv = SETTINGS["server"]
    uvicorn.run(app, host=srv.host, port=srv.port, log_level=logging.INFO)
