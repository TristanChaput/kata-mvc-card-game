from typing import List
from models.deck import Deck
from models.player import Player
from views.view import IView


class Game:

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
        for player in self._players:
            player.add_a_card_in_hand(card=cards.pop())

    def show_cards(self) -> None:
        for player in self._players:
            player.flip_hand()
            self._view.show_player_hand(player=player)

    def check_for_a_winner(self) -> Player:
        winner = self.get_a_player(index=0)
        for player in self._players[1:]:
            winner_card = winner.get_a_card_in_hand(index=0)
            player_card = player.get_a_card_in_hand(index=0)

            if winner_card.rank.weight == player_card.rank.weight:
                if winner_card.suit.weight < player_card.suit.weight:
                    winner = player
            elif winner_card.rank.weight < player_card.rank.weight:
                winner = player
        return winner

    def run(self):
        self.register_players()
        self.give_a_card()
        self.show_cards()
        winner = self.check_for_a_winner()
        self._view.show_winner(player=winner)
