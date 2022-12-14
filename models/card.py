class Suit:
    def __init__(self, weight: int, symbol: str) -> None:
        self.weight = weight
        self.symbol = symbol


class Rank:
    def __init__(self, weight: int, symbol: str) -> None:
        self.weight = weight
        self.symbol = symbol

    def __eq__(self, __o: object) -> bool:
        return self.weight == __o.weight and self.symbol == __o.symbol


class Card:
    def __init__(self, suit: Suit, rank: Rank) -> None:
        self._suit = suit
        self._rank = rank
        self.face_up = False

    def flip(self) -> None:
        self.face_up = not self.face_up

    def is_turned_down(self) -> bool:
        return not self.face_up

    @property
    def rank(self) -> Rank:
        return self._rank

    @property
    def suit(self) -> Suit:
        return self._suit

    def __str__(self) -> str:
        return self.rank.symbol + self.suit.symbol

    def __eq__(self, __o: object) -> bool:
        return self.rank == __o.rank and self.suit == __o.suit

    def __hash__(self):
        return hash((self._rank, self._suit, self.face_up))
