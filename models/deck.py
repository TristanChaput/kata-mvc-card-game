from random import shuffle
from typing import List
from models.card import Card


class Deck:
    SUITS = [
        "♠",
        "♣",
        "♥",
        "♦",
    ]

    RANKS = [
        "A",
        "K",
        "Q",
        "J",
        "10",
        "9",
        "8",
        "7",
        "6",
        "5",
        "4",
        "3",
        "2",
    ]

    _cards: List[Card]

    def __init__(self) -> None:
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                self._cards.append(Card(suit, rank))

    def get_cards(self) -> List[Card]:
        return self._cards

    def shuffle(self) -> None:
        shuffle(self._cards)
