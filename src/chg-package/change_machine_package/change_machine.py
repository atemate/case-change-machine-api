from typing import TypedDict

from .algorithms import calculate_change, count_items
from .currency import (
    EUR_COINS_IN_CENTS,
    EUR_DENOMINATIONS_IN_CENTS,
    TDenomination,
    to_eur_unit,
)
from .exceptions import InsertedNotEnoughError
from .utils import cast_to_int_or_fail


class TCoins(TDenomination):
    """Type for storing `count` coins/banknotes of the same value."""

    count: int


class TChange(TypedDict):
    """Type for storing the change - the output of the service."""

    total_coins: float
    total_eur: float
    coins: list[TCoins]


def get_change_cents(eur_inserted: float, price_eur: float) -> int:
    # Note: to avoid having 0.99999... instead of 1, convert each to cents individually
    input_cents = cast_to_int_or_fail(eur_inserted * 100, "cents inserted")
    price_cents = cast_to_int_or_fail(price_eur * 100, "price in cents")
    change_cents = input_cents - price_cents
    return change_cents


def return_coins(
    product_price_eur: float,
    eur_inserted: float,
    algorithm: str = "greedy_search",
    return_coins_only: bool = True,
) -> TChange:
    if eur_inserted < product_price_eur:
        raise InsertedNotEnoughError(product_price_eur, eur_inserted)

    denominations = (
        EUR_COINS_IN_CENTS if return_coins_only else EUR_DENOMINATIONS_IN_CENTS
    )
    change_cents = get_change_cents(eur_inserted, product_price_eur)

    change_cent_coins = calculate_change(
        change_cents,
        denominations,
        algorithm=algorithm,
    )
    change_coins: list[TCoins] = [
        {
            "count": count,
            **to_eur_unit(cents),  # type: ignore
        }
        for cents, count in count_items(change_cent_coins).items()
    ]
    change_coins.sort(key=lambda coin: coin["value_in_cents"], reverse=True)

    total_coins = sum(c["count"] for c in change_coins)
    total_eur = sum(c["value_in_cents"] * c["count"] for c in change_coins) / 100
    return {
        "total_coins": total_coins,
        "total_eur": total_eur,
        "coins": change_coins,
    }
