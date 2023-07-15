from collections import Counter

from .exceptions import ChangeImpossibleError


def greedy_change(
    amount: int, coins: list[int], force_reverse_coins: bool = False
) -> list[int]:
    """
    Given the amount of money to exchange and the list of existing coins
    sorted from largest to smallest, return the list of coins to exchange
    the given amount. Coins can repeate multiple times.
    """
    if amount < 0:
        raise ValueError(f"Cannot give change for negative amount: {amount}")

    change = []
    if force_reverse_coins:
        # Not to be sorted on each function call
        coins = sorted(coins, reverse=True)

    for coin in coins:
        while coin <= amount:
            amount -= coin
            change.append(coin)

    if amount == 0:
        return change

    raise ChangeImpossibleError(amount, coins)


def count_items(items: list[int]) -> dict[int, int]:
    """
    Given a list of items with repetition, return the dict mapping
    each item to its count in the given list:
    >>> count_items([1, 1, 1, 2, 2, 3])
    {1: 3, 2: 2, 3: 1}
    >>> count_items([])
    {}
    """
    return dict(Counter(items))
