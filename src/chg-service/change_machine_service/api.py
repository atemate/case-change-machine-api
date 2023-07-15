from functools import lru_cache
from typing import Annotated, Any

from change_machine_package import return_coins
from fastapi import Depends, FastAPI

from .exceptions import register_exception_handlers
from .logger import log
from .settings import ChangeMachineSettings

app = FastAPI()
register_exception_handlers(app)


@lru_cache()
def get_chg_settings():
    return ChangeMachineSettings()


@app.get("/health")
def health():
    return {}


@app.get("/info")
async def info(
    chg_settings: Annotated[ChangeMachineSettings, Depends(get_chg_settings)]
):
    return {
        "change_machine": {
            "algorithm": chg_settings.algorithm,
            "return_coins_only": chg_settings.return_coins_only,
        },
    }


@app.get("/pay")
def read_item(
    currywurst_price_eur: float,
    eur_inserted: float,
    chg_settings: Annotated[ChangeMachineSettings, Depends(get_chg_settings)],
):
    kwargs: dict[str, Any] = dict(
        currywurst_price_eur=currywurst_price_eur,
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
