from typing import List
from models.card import Card
from uuid import uuid4


class Player:
    def __init__(self, name: str) -> None:
        self.id = uuid4()
        self.name: str = name
        self.hand: List[Card] = []

    def get_a_card_in_hand(self, index: int) -> Card:
        return self.hand[index]

    def add_a_card_in_hand(self, card: Card) -> None:
        self.hand.append(card)

    def flip_hand(self) -> None:
        for card in self.hand:
            card.flip()

    def __eq__(self, __o: object) -> bool:
        return self.name == __o.name
