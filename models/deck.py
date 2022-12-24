from random import shuffle
from typing import List
from models.card import Card, Rank, Suit


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

    def __init__(self) -> None:
        self.cards: List[Card] = []
        for weight_suit, suit in self.SUITS.items():
            for weight_rank, rank in self.RANKS.items():
                self.cards.append(
                    Card(
                        Suit(weight_suit, suit),
                        Rank(weight_rank, rank),
                    )
                )

    def get_cards(self) -> List[Card]:
        return self.cards

    def shuffle(self) -> None:
        shuffle(self.cards)
