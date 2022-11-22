class Card:
    suit = str
    rank = str

    def __init__(self, suit: str, rank: str) -> None:
        self.suit: str = suit
        self.rank: str = rank

    def __eq__(self, __o: object) -> bool:
        return self.suit == __o.suit and self.rank == __o.rank
