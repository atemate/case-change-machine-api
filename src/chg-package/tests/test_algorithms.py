import pytest
from change_machine_package.algorithms import calculate_change, count_items
from change_machine_package.exceptions import ChangeImpossibleError

ALGORITHMS = ["greedy_search", "dynamic_programming"]
COINS_3 = [10, 5, 1]
COINS_4 = [10, 5, 2, 1]
COINS_INCOMPLETE = [10, 5, 2]


@pytest.mark.parametrize("algorithm", ALGORITHMS)
@pytest.mark.parametrize(
    "amount, coins, expected",
    [
        # one set of coins:
        (2, COINS_3, [1, 1]),
        (6, COINS_3, [5, 1]),
        (7, COINS_3, [5, 1, 1]),
        (11, COINS_3, [10, 1]),
        (14, COINS_3, [10, 1, 1, 1, 1]),
        (15, COINS_3, [10, 5]),
        # different set of coins:
        (2, COINS_4, [2]),
        (6, COINS_4, [5, 1]),
        (7, COINS_4, [5, 2]),
        (8, COINS_4, [5, 2, 1]),
        (11, COINS_4, [10, 1]),
        (14, COINS_4, [10, 2, 2]),
        (15, COINS_4, [10, 5]),
        (6, COINS_4, [5, 1]),
        (5, COINS_4, [5]),
        (4, COINS_4, [2, 2]),
        (3, COINS_4, [2, 1]),
        (2, COINS_4, [2]),
        (0, COINS_4, []),
        (0, COINS_INCOMPLETE, []),
        (2, COINS_INCOMPLETE, [2]),
        (4, COINS_INCOMPLETE, [2, 2]),
        (7, COINS_INCOMPLETE, [5, 2]),
        (9, COINS_INCOMPLETE, [5, 2, 2]),
        (12, COINS_INCOMPLETE, [10, 2]),
        (14, COINS_INCOMPLETE, [10, 2, 2]),
        (14, COINS_INCOMPLETE, [10, 2, 2]),
        (17, COINS_INCOMPLETE, [10, 5, 2]),
    ],
)
def test_calculate_change_ok(
    amount: int,
    coins: list[int],
    expected: list[int],
    algorithm: str,
) -> None:
    actual = calculate_change(amount, coins, algorithm=algorithm)
    assert actual == expected


@pytest.mark.parametrize(
    "amount, coins, expected",
    [
        (6, COINS_INCOMPLETE, [2, 2, 2]),
        (11, COINS_INCOMPLETE, [5, 2, 2, 2]),
        (13, COINS_INCOMPLETE, [5, 2, 2, 2, 2]),
        (16, COINS_INCOMPLETE, [10, 2, 2, 2]),
    ],
)
def test_calculate_change_only_greedy_fails(
    amount: int,
    coins: list[int],
    expected: list[int],
) -> None:
    # greedy fails
    with pytest.raises(ChangeImpossibleError):
        calculate_change(amount, coins, algorithm="greedy_search")
    # dynamic works
    actual = calculate_change(amount, coins, algorithm="dynamic_programming")
    assert actual == expected


@pytest.mark.parametrize("algorithm", ALGORITHMS)
@pytest.mark.parametrize(
    "amount, coins",
    [
        # one set of coins:
        (1, COINS_INCOMPLETE),
        (3, COINS_INCOMPLETE),
    ],
)
def test_calculate_change_fail_incomplete(
    amount: int,
    coins: list[int],
    algorithm: str,
) -> None:
    with pytest.raises(ChangeImpossibleError):
        calculate_change(amount, coins, algorithm=algorithm)


@pytest.mark.parametrize(
    "items, expected",
    [
        ([], {}),
        ([1, 2, 3, 1, 2, 1], {1: 3, 2: 2, 3: 1}),
        ([5, 4, 3] * 100, {3: 100, 4: 100, 5: 100}),
    ],
)
def test_count_items(items: list[int], expected: dict[int, int]) -> None:
    actual = count_items(items)
    assert actual == expected
