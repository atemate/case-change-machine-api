from .conftest import get_chg_settings_override


def test_get_health(client):
    resp = client.get("/api/v1/health")
    data = resp.json()
    assert resp.status_code == 200, data
    assert data == {}


def test_get_info(client):
    chg_settings = get_chg_settings_override()
    resp = client.get("/api/v1/info")
    data = resp.json()
    assert resp.status_code == 200, data
    assert data == {"change_machine": dict(chg_settings)}


def test_get_pay(client):
    resp = client.get(
        "/api/v1/pay", params={"currywurst_price_eur": 4.9, "eur_inserted": 10}
    )
    data = resp.json()
    assert resp.status_code == 200, data
    assert data == [
        {"count": 2, "value": 2, "value_in_cents": 200, "name": "euro", "type": "coin"},
        {"count": 1, "value": 1, "value_in_cents": 100, "name": "euro", "type": "coin"},
        {"count": 1, "value": 10, "value_in_cents": 10, "name": "cent", "type": "coin"},
    ]
