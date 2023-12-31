from typing import TypedDict


class TDenomination(TypedDict):
    """Type for storing a `type` coin/banknote of value `value`
    equal to value in cents `value_in_cents`
    """

    name: str
    type: str
    value: int
    value_in_cents: int


EUR_DENOMINATIONS: list[TDenomination] = [
    {"value": 1, "value_in_cents": 1, "name": "cent", "type": "coin"},
    {"value": 2, "value_in_cents": 2, "name": "cent", "type": "coin"},
    {"value": 5, "value_in_cents": 5, "name": "cent", "type": "coin"},
    {"value": 10, "value_in_cents": 10, "name": "cent", "type": "coin"},
    {"value": 20, "value_in_cents": 20, "name": "cent", "type": "coin"},
    # {"value": 25, "value_in_cents": 25,, "name": "quarter","type": "coin"},
    {"value": 50, "value_in_cents": 50, "name": "cent", "type": "coin"},
    {"value": 1, "value_in_cents": 100, "name": "euro", "type": "coin"},
    {"value": 2, "value_in_cents": 200, "name": "euro", "type": "coin"},
    {"value": 5, "value_in_cents": 500, "name": "euro", "type": "banknote"},
    {"value": 10, "value_in_cents": 1000, "name": "euro", "type": "banknote"},
    {"value": 20, "value_in_cents": 2000, "name": "euro", "type": "banknote"},
    {"value": 50, "value_in_cents": 5000, "name": "euro", "type": "banknote"},
    {"value": 100, "value_in_cents": 10000, "name": "euro", "type": "banknote"},
    {"value": 200, "value_in_cents": 20000, "name": "euro", "type": "banknote"},
    {"value": 500, "value_in_cents": 50000, "name": "euro", "type": "banknote"},
]


EUR_DENOMINATIONS_IN_CENTS: list[int] = sorted(
    [x["value_in_cents"] for x in EUR_DENOMINATIONS],
    reverse=True,
)

EUR_COINS_IN_CENTS: list[int] = sorted(
    [x["value_in_cents"] for x in EUR_DENOMINATIONS if x["type"] == "coin"],
    reverse=True,
)


def to_eur_unit(value_in_cents: int) -> TDenomination:
    for coin in EUR_DENOMINATIONS:
        if coin["value_in_cents"] == value_in_cents:
            return coin
    raise ValueError(f"Coin of value in cents {repr(value_in_cents)} not found")
