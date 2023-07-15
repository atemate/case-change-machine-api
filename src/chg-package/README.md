# Internals package for the Change Machine

## Requirements

### Functional requirements
Function `return_coins()`:
- accepts only two arguments, `currywurst_price` and `eur_inserted` (stateless: has infinite amount of each coin and banknote inside),
- accepts accepts any coins or banknotes but returns only coins and works only with EUR currency:
    - [coins denominations](https://www.ecb.europa.eu/euro/coins/html/index.en.html):
        - cents: 1, 2, 5, 10, 20, 50
        - euros: 1, 2
    - [banknotes denominations](https://www.ecb.europa.eu/euro/banknotes/html/index.en.html):
        - euros: 5, 10, 20, 50, 100, 200, 500
- returns the lowest amount of coins possible,
- returns a single data structure with the correct amount of coins to return for change,
- works for any positive number.


### Nonfunctional requirements
- execution time: for any number <= €1000, execution time should be <1 sec
- code extensible ?

If the service is to be scaled for many currywurst machines:
- scalable ?


### Ideas for improvements
- allow giving out banknotes as change
- stateful (has limited amount of coins and banknotes)
- forbids accepting several banknotes (e.g. €500)
- works with different pre-defined currencies (e.g. USD, CHF, RUR)
- would offer multiple sets of change for user to choose (e.g. €50 can be returned as a single banknote €50 or as €20+€20+€10 or as €10*5, and each of them might be useful by the user in different situations)
- would operate in different modes optimising different metrics without asking the user (e.g. returning minimal amount of coins but maximal amount of banknotes - sometimes in Berlin it's useful to have more €10 and €20 banknotes rather than €50 and €100)

Note that as the change-making problem is weakly NP-hard (depends on the currency system and algorithm), some algorithms implemented for some task extensions would be non-polynomial.


## Algorithms
The task is the change-making problem, a special case of the integer knapsack problem, is weakly NP-hard.

### Greedy method
See implementation in `greedy_change()`.

The idea is to keep selecting the largest denomination coins/notes available to represent a given amount of money, gradually reducing the amount until it reaches zero. The greedy method is already optimal for the Euro currency, but might give non-optimal solutions for other currencies.

