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

    cards: List[Card]

    def __init__(self) -> None:
        self.cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.cards.append(Card(suit, rank))

    def get_cards(self) -> List[Card]:
        return self.cards
