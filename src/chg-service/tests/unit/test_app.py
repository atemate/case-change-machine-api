from change_machine_service.settings import get_settings


def test_get_health(client):
    resp = client.get("/api/v1/health")
    data = resp.json()
    assert resp.status_code == 200, data
    assert data == {}


def test_get_info(client):
    settings = get_settings()
    srv = settings["server"]
    chg = settings["change_machine"]
    resp = client.get("/api/v1/info")
    data = resp.json()
    # print(data)
    assert resp.status_code == 200, data
    assert data == {
        "server": {
            "prefix": srv.prefix,
            "host": srv.host,
            "port": srv.port,
            "log_file": srv.log_file,
        },
        "change_machine": {
            "algorithm": chg.algorithm,
            "return_coins_only": chg.return_coins_only,
        },
    }


def test_get_pay(client):
    resp = client.get(
        "/api/v1/pay", params={"product_price_eur": 4.9, "eur_inserted": 10}
    )
    data = resp.json()
    assert resp.status_code == 200, data
    assert data == {
        "total_coins": 4,
        "total_eur": 5.1,
        "coins": [
            {
                "count": 2,
                "value": 2,
                "value_in_cents": 200,
                "name": "euro",
                "type": "coin",
            },
            {
                "count": 1,
                "value": 1,
                "value_in_cents": 100,
                "name": "euro",
                "type": "coin",
            },
            {
                "count": 1,
                "value": 10,
                "value_in_cents": 10,
                "name": "cent",
                "type": "coin",
            },
        ],
    }
