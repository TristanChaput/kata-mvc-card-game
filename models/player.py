from typing import List
from models.card import Card


class Player:

    _name: str
    _hand: List[Card]

    def __init__(self, name: str) -> None:
        self._name: str = name
        self._hand: List[Card] = []

    def get_name(self) -> str:
        return self._name

    def get_hand(self) -> List[Card]:
        return self._hand

    def add_a_card_in_hand(self, card: Card) -> None:
        self._hand.append(card)

    def __eq__(self, __o: object) -> bool:
        return self._name == __o._name
