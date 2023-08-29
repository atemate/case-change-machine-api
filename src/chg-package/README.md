# Implementation package for the Change Machine

## Requirements

### Functional requirements
Function `return_coins()`:
- accepts only two arguments, `product_price` and `eur_inserted` (stateless: has infinite amount of each coin and banknote inside),
- accepts accepts any coins or banknotes but returns only coins and works only with EUR currency:
    - [coins denominations](https://www.ecb.europa.eu/euro/coins/html/index.en.html):
        - cents: 1, 2, 5, 10, 20, 50
        - euros: 1, 2
    - [banknotes denominations](https://www.ecb.europa.eu/euro/banknotes/html/index.en.html):
        - euros: 5, 10, 20, 50, 100, 200, 500
- returns the lowest amount of coins possible,
- returns a single data structure with the correct amount of coins to return for change,
- works for any positive number.

> Note: we assume that in EUR currency it is possible to form any number with coins and banknotes, so we allow any values in `eur_inserted`.


### Nonfunctional requirements
- execution time: for any number <= €1000, execution time should be <1 sec
- code extensible ?

If the service is to be scaled for many product machines:
- scalable ?


### Ideas for future improvements
- allow giving out banknotes as change
- stateful (has limited amount of coins and banknotes)
- forbids accepting several banknotes (e.g. €500)
- works with different pre-defined currencies (e.g. USD, CHF, RUR)
- would offer multiple sets of change for user to choose (e.g. €50 can be returned as a single banknote €50 or as €20+€20+€10 or as €10*5, and each of them might be useful by the user in different situations)
- would operate in different modes optimising different metrics without asking the user (e.g. returning minimal amount of coins but maximal amount of banknotes - sometimes in Berlin it's useful to have more €10 and €20 banknotes rather than €50 and €100)

Note that as the change-making problem is weakly NP-hard (depends on the currency system and algorithm), some algorithms implemented for some task extensions would be non-polynomial.


## Algorithms
The task is the change-making problem, a special case of the integer knapsack problem, is weakly NP-hard.
A simple greedy algorithm finds not-always-optimal solution, but is good enough to cover most of the typical cases.

### Greedy method
See implementation `greedy_change()` in [src/chg-package/change_machine_package/algorithms.py](src/chg-package/change_machine_package/algorithms.py)

The idea is to keep selecting the largest denomination coins/notes available to represent a given amount of money, gradually reducing the amount until it reaches zero. The greedy method is already optimal for the Euro currency, but might give non-optimal solutions for other currencies.

The time complexity of this algorithm is `O(L)`, where `L` is the number of available coin denominations.

However, it is important to note that the greedy strategy may not always provide the optimal solution in terms of the minimal number of coins. There may be cases where the greedy approach fails to find the globally optimal solution and instead provides a suboptimal result.


### Dynamic programming method
See implementation `dynamic_programming_change()` in [src/chg-package/change_machine_package/algorithms.py](src/chg-package/change_machine_package/algorithms.py)

The algorithm uses dynamic programming to find the minimal number of coins needed to make change for a given amount:
- it constructs a matrix where each cell represents the minimal number of coins required to make change for a specific amount using available coin denominations.
- by iteratively considering each coin denomination and amount, the algorithm fills the matrix by choosing the minimum between using the current coin or excluding it.
- finally, it backtracks from the bottom-right corner of the matrix to reconstruct the coins used by following the path that leads to the minimal change.

This algorithm is more robust for several corner cases than greedy search algorithm, for example it will be able to find the change `[2, 2, 2]` for amount `6` out of possible coins `[10, 5, 2]`, whereas the greedy search algorithm will fail on finding `[5, 2]` (see test `test_calculate_change_only_greedy_fails` in [src/chg-package/tests/test_algorithms.py](src/chg-package/tests/test_algorithms.py)). Due to our comprehensive unit testing of the first (greedy) algorithm and the effective choice of abstractions using functions over objects or structs, we were able to easily test both algorithms. This was done by using pytest parametrisation: `@pytest.mark.parametrize("algorithm", ALGORITHMS)`.

The time complexity of this algorithm is `O(n * L)`, where `n` is the given amount and `L` is the number of available coin denominations.
