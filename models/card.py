from typing import Tuple


class Suit:
    def __init__(self, weight: int, symbol: str) -> None:
        self.weight = weight
        self.symbol = symbol


class Rank:
    def __init__(self, weight: int, symbol: str) -> None:
        self.weight = weight
        self.symbol = symbol


class Card:
    def __init__(self, suit: Suit, rank: Rank) -> None:
        self._suit = suit
        self._rank = rank
        self._face_up = False

    def flip(self) -> None:
        self._face_up = not self._face_up

    def is_turned_down(self) -> bool:
        return not self._face_up

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
