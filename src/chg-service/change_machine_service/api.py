from fastapi import FastAPI

from .config import get_config

cfg = get_config()
app = FastAPI()


@app.get("/health")
def health():
    return {}


@app.get("/pay")
def read_item(currywurst_price_eur: float, eur_inserted: float):

    return {"currywurst_price_eur": currywurst_price_eur, "eur_inserted": eur_inserted}
