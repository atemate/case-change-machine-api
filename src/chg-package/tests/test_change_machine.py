import pytest
from change_machine_package.change_machine import get_change_cents, return_coins

ALGORITHMS = ["greedy_search", "dynamic_programming"]


@pytest.mark.parametrize(
    "eur_inserted, price_eur, expected_cents",
    [
        (10, 0.5, 950),
        (10, 0.99, 901),
        (100, 0.99, 9901),
        (10000, 0.99, 999901),
        (1000000, 0.99, 99999901),
        (100000000, 0.99, 9999999901),
        (100, 0, 10000),
        (0, 5, -500),  # negative change will be disallowed by the algorithm
        (0, 0, 0),
        (10, 4.9, 510),  # test for python bug: 4.9 * 100 == 490.00000000000006
    ],
)
def test_get_change_cents(
    eur_inserted: float,
    price_eur: float,
    expected_cents: int,
):
    actual_cents = get_change_cents(eur_inserted, price_eur)
    assert actual_cents == expected_cents


@pytest.mark.parametrize("algorithm", ALGORITHMS)
def test_count_items_return_coins_only_true(algorithm: str) -> None:
    currywurst_price_eur = 1.23
    eur_inserted = 500

    actual = return_coins(
        currywurst_price_eur=currywurst_price_eur,
        eur_inserted=eur_inserted,
        algorithm=algorithm,
        return_coins_only=True,
    )
    assert actual == {
        "total_coins": 253,
        "total_eur": 498.77,
        "coins": [
            {
                "count": 249,
                "name": "euro",
                "type": "coin",
                "value": 2,
                "value_in_cents": 200,
            },
            {
                "count": 1,
                "name": "cent",
                "type": "coin",
                "value": 50,
                "value_in_cents": 50,
            },
            {
                "count": 1,
                "name": "cent",
                "type": "coin",
                "value": 20,
                "value_in_cents": 20,
            },
            {
                "count": 1,
                "name": "cent",
                "type": "coin",
                "value": 5,
                "value_in_cents": 5,
            },
            {
                "count": 1,
                "name": "cent",
                "type": "coin",
                "value": 2,
                "value_in_cents": 2,
            },
        ],
    }


@pytest.mark.parametrize("algorithm", ALGORITHMS)
def test_count_items_return_coins_only_false(algorithm: str) -> None:
    currywurst_price_eur = 1.23
    eur_inserted = 500

    actual = return_coins(
        currywurst_price_eur=currywurst_price_eur,
        eur_inserted=eur_inserted,
        algorithm=algorithm,
        return_coins_only=False,
    )
    assert actual == {
        "total_coins": 12,
        "total_eur": 498.77,
        "coins": [
            {
                "count": 2,
                "name": "euro",
                "type": "banknote",
                "value": 200,
                "value_in_cents": 20000,
            },
            {
                "count": 1,
                "name": "euro",
                "type": "banknote",
                "value": 50,
                "value_in_cents": 5000,
            },
            {
                "count": 2,
                "name": "euro",
                "type": "banknote",
                "value": 20,
                "value_in_cents": 2000,
            },
            {
                "count": 1,
                "name": "euro",
                "type": "banknote",
                "value": 5,
                "value_in_cents": 500,
            },
            {
                "count": 1,
                "name": "euro",
                "type": "coin",
                "value": 2,
                "value_in_cents": 200,
            },
            {
                "count": 1,
                "name": "euro",
                "type": "coin",
                "value": 1,
                "value_in_cents": 100,
            },
            {
                "count": 1,
                "name": "cent",
                "type": "coin",
                "value": 50,
                "value_in_cents": 50,
            },
            {
                "count": 1,
                "name": "cent",
                "type": "coin",
                "value": 20,
                "value_in_cents": 20,
            },
            {
                "count": 1,
                "name": "cent",
                "type": "coin",
                "value": 5,
                "value_in_cents": 5,
            },
            {
                "count": 1,
                "name": "cent",
                "type": "coin",
                "value": 2,
                "value_in_cents": 2,
            },
        ],
    }
