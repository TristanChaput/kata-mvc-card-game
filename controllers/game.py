from typing import List
from models.deck import Deck
from models.player import Player
from views.view import IView


class Game:

    _players: List[Player]
    _deck: Deck
    _view: IView
    MAX_PLAYERS_ALLOWED = 5

    def __init__(self, view: IView) -> None:
        self._players: List[Player] = []
        self._deck: Deck = Deck()
        self._deck.shuffle()
        self._view: IView = view

    def register_players(self) -> None:
        while len(self._players) < self.MAX_PLAYERS_ALLOWED:
            name = self._view.player_register_name()
            if not name:
                return
            self._players.append(Player(name=name))

    def get_a_player(self, index) -> Player:
        return self._players[index]

    def get_players(self) -> List[Player]:
        return self._players

    def give_a_card(self) -> None:
        cards = self._deck.get_cards()
        for i, player in enumerate(self._players):
            player.add_a_card_in_hand(cards[i])

    def show_cards(self) -> None:
        for player in self._players:
            player.flip_hand()
            player_card = player.get_hand()[0]
            self._view.show_player_hand(player_card)
