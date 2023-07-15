from typing import Any

from .algorithms import count_items, greedy_change
from .currency import EUR_COINS_IN_CENTS, EUR_DENOMINATIONS_IN_CENTS, to_eur_unit
from .utils import cast_to_int_or_fail


def return_coins(
    currywurst_price_eur: float,
    eur_inserted: float,
    algorithm: str = "greedy",
    return_coins_only: bool = True,
) -> list[dict[str, Any]]:
    denominations = (
        EUR_COINS_IN_CENTS if return_coins_only else EUR_DENOMINATIONS_IN_CENTS
    )

    # Note: to avoid having 0.99999... instead of 1, convert each to cents individually
    cents_inserted = cast_to_int_or_fail(eur_inserted * 100, "cents inserted")
    currywurst_price_cents = cast_to_int_or_fail(
        currywurst_price_eur * 100, "currywurst price in cents"
    )
    change_cents = cents_inserted - currywurst_price_cents

    if algorithm == "greedy":
        change_cent_coins = greedy_change(change_cents, denominations)
    else:
        raise NotImplementedError(algorithm)

    change_coins = sorted(
        [
            (count, to_eur_unit(cents))
            for cents, count in count_items(change_cent_coins).items()
        ],
        key=lambda pair: -pair[1]["value_in_cents"],
    )

    # summa = sum(c*x["value_in_cents"] for c,x in coins)
    # assert summa == amount_cents, (summa, amount_cents)
    return [
        {
            "count": count,
            "value": coin["value"],
            "name": coin["name"],
            "type": coin["type"],
        }
        for count, coin in change_coins
    ]
