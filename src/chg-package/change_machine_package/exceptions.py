class ChangeErrorBase(ValueError):
    pass


class ChangeImpossibleError(ChangeErrorBase):
    def __init__(self, amount: float, coins: list[int]):
        super().__init__(f"Change of amount {amount} is impossible with coins {coins}")
        self.amount = amount
        self.coins = coins


class InsertedNotEnoughError(ChangeErrorBase):
    def __init__(self, amount: float, inserted: float):
        super().__init__(f"Required amount {amount} but inserted only {inserted}")
        self.amount = amount
        self.inserted = inserted
