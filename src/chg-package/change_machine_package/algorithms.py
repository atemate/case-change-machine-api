from collections import Counter
from typing import Any

import numpy as np

from .exceptions import ChangeImpossibleError
from .logging import log


def calculate_change(
    amount: int, coins: list[int], algorithm: str = "greedy_search"
) -> list[int]:
    if algorithm == "greedy_search":
        return greedy_change(amount, coins)
    if algorithm == "dynamic_programming":
        return dynamic_programming_change(amount, coins)
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

    log.error(
        f"[greedy_algorithm] cannot get change of {amount} with coins {coins}: "
        f"my best guess is {repr(sum(change))} which is comprised from {change}"
    )
    raise ChangeImpossibleError(amount, coins)


def _get_zeros_matrix(coins: list[int], n: int) -> np.ndarray[float, float]:
    """Creates matrix:
    array([[0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0.]])
    """
    return np.zeros((len(coins) + 1, n + 1), dtype=float)


def _get_change_making_matrix(
    coins: list[int], n: int
) -> np.ndarray[Any, np.dtype[Any]]:
    """Creates matrix:
    array([[ 0., inf, inf, inf, inf, inf, inf],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.]])
    """
    M = _get_zeros_matrix(coins, n)
    M[0, 1:] = np.inf
    return M


def dynamic_programming_change(amount: int, coins: list[int]) -> list[int]:
    n = amount
    M = _get_change_making_matrix(coins, n)  # change matrix
    U = _get_zeros_matrix(coins, n)  # used coins

    for c, coin in enumerate(coins, 1):
        for r in range(1, n + 1):
            # Just use the coin
            if coin == r:
                M[c, r] = 1
                U[c, r] = coin
            # coin cannot be included.
            # Use the previous solution for making r,
            # excluding coin:
            elif coin > r:
                M[c, r] = M[c - 1, r]
                U[c, r] = U[c - 1, r]
            # coin can be used:
            # Decide which one of the following solutions is the best:
            # 1. Using the previous solution for making r (without using coin).
            # 2. Using the previous solution for making r - coin (without
            #      using coin) plus this 1 extra coin.
            else:
                if M[c - 1, r] < M[c, r - coin] + 1:
                    M[c, r] = M[c - 1, r]
                    U[c, r] = U[c - 1, r]
                else:
                    M[c, r] = M[c, r - coin + 1]
                    U[c, r] = coin
                M[c, r] = min(M[c - 1, r], M[c, r - coin] + 1)

    # Reconstruct the coins used
    change = []
    c = len(coins)
    r = n
    while c > 0 and r > 0:
        val = int(U[c, r])
        if val == 0:
            c -= 1
        else:
            change.append(val)
            r -= val

    change = change[::-1]
    summa = sum(change)
    if summa != n:
        log.error(
            f"[dynamic_programming] cannot get change of {n} with coins {coins}: "
            f"my best guess is {repr(summa)} which is comprised from {change}"
        )
        raise ChangeImpossibleError(n, coins)
    return change


# def dynamic_programming_change(amount: int, coins: list[int]) -> list[int]:
#     M = _get_change_making_matrix(coins, amount)
#     used_coins = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]

#     for c, coin in enumerate(coins, 1):
#         for r in range(1, amount + 1):
#             # Just use the coin
#             if coin == r:
#                 M[c][r] = 1
#                 used_coins[c][r] = coin
#             # coin cannot be included.
#             # Use the previous solution for making r,
#             # excluding coin:
#             elif coin > r:
#                 M[c][r] = M[c - 1][r]
#                 used_coins[c][r] = used_coins[c - 1][r]
#             # coin can be used:
#             # Decide which one of the following solutions is the best:
#             # 1. Using the previous solution for making r (without using coin).
#             # 2. Using the previous solution for making r - coin (without
#             #      using coin) plus this 1 extra coin.
#             else:
#                 if M[c - 1][r] < M[c][r - coin] + 1:
#                     M[c][r] = M[c - 1][r]
#                     used_coins[c][r] = used_coins[c - 1][r]
#                 else:
#                     M[c][r] = M[c][r - coin + 1]
#                     used_coins[c][r] = coin

#                 M[c][r] = min(M[c - 1][r], M[c][r - coin] + 1)

#     # Reconstruct the coins used
#     coins_used = []
#     c = len(coins)
#     r = amount
#     while c > 0 and r > 0:
#         if used_coins[c][r] == 0:
#             c -= 1
#         else:
#             coins_used.append(used_coins[c][r])
#             r -= used_coins[c][r]

#     change = coins_used[::-1]
#     if sum(change) != amount:
#         raise ChangeImpossibleError(amount, coins)
#     return change


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
