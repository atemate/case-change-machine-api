class ChangeImpossibleError(ValueError):
    def __init__(self, amount: int, coins: list[int]):
        super().__init__(f"Change of amount {amount} is impossible with coins {coins}")
        self.amount = amount
        self.coins = coins
