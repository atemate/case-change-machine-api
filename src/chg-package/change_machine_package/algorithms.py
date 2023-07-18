from collections import Counter

from .exceptions import ChangeImpossibleError


def calculate_change(
    amount: int, coins: list[int], algorithm: str = "greedy"
) -> list[int]:
    if algorithm == "greedy":
        return greedy_change(amount, coins)
    raise NotImplementedError(algorithm)


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


def _get_change_making_matrix(set_of_coins, r: int):
    M = [[0 for _ in range(r + 1)] for _ in range(len(set_of_coins) + 1)]
    for i in range(1, r + 1):
        M[0][i] = float("inf")  # By default there is no way of making change
    return M


def dynamic_programming_change(
    coins: list[int],
    amount: int,
) -> list[int]:
    M = _get_change_making_matrix(coins, amount)
    for c, coin in enumerate(coins, 1):
        for r in range(1, amount + 1):
            # Just use the coin
            if coin == r:
                M[c][r] = 1
            # coin cannot be included.
            # Use the previous solution for making r,
            # excluding coin
            elif coin > r:
                M[c][r] = M[c - 1][r]
            # coin can be used.
            # Decide which one of the following solutions is the best:
            # 1. Using the previous solution for making r (without using coin).
            # 2. Using the previous solution for making r - coin (without
            #      using coin) plus this 1 extra coin.
            else:
                M[c][r] = min(M[c - 1][r], 1 + M[c][r - coin])
    return M[-1][-1]


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
