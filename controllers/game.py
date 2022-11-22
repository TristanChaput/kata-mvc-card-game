from typing import List
from models.deck import Deck
from models.player import Player


class Game:

    _players: List[Player]
    _deck: Deck

    def __init__(self, players) -> None:
        if len(players) > 5:
            raise Exception("To many players")
        self._players = players
        self._deck = Deck()
        self._deck.shuffle()

    def get_players(self) -> List[Player]:
        return self._players

    def give_a_card(self) -> None:
        cards = self._deck.get_cards()
        for i, player in enumerate(self._players):
            player.add_a_card_in_hand(cards[i])
