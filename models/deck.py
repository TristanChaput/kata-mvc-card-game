from random import shuffle
from typing import List
from models.card import Card


class Deck:

    SUITS = {
        4: "♣",
        3: "♠",
        2: "♥",
        1: "♦",
    }

    RANKS = {
        14: "A",
        13: "K",
        12: "Q",
        11: "J",
        10: "10",
        9: "9",
        8: "8",
        7: "7",
        6: "6",
        5: "5",
        4: "4",
        3: "3",
        2: "2",
    }

    _cards: List[Card]

    def __init__(self) -> None:
        self._cards: List[Card] = []
        for weight, suit in self.SUITS.items():
            for weight, rank in self.RANKS.items():
                self._cards.append(
                    Card(
                        (weight, suit),
                        (weight, rank),
                    )
                )

    def get_cards(self) -> List[Card]:
        return self._cards

    def shuffle(self) -> None:
        shuffle(self._cards)
