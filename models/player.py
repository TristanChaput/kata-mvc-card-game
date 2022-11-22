from typing import List
from models.card import Card


class Player:

    _name: str
    _hand: List[Card]

    def __init__(self, name) -> None:
        self._name = name
        self._hand = []

    def get_name(self):
        return self._name

    def get_hand(self):
        return self._hand

    def add_a_card_in_hand(self, card):
        self._hand.append(card)
