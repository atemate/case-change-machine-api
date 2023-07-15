import pytest
from change_machine_package.algorithms import calculate_change, count_items
from change_machine_package.exceptions import ChangeImpossibleError

ALGORITHMS = ["greedy"]
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


@pytest.mark.parametrize("algorithm", ALGORITHMS)
@pytest.mark.parametrize(
    "amount, coins",
    [
        # one set of coins:
        (1, COINS_INCOMPLETE),
        (3, COINS_INCOMPLETE),
        (6, COINS_INCOMPLETE),
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
