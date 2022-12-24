from typing import List
from models.deck import Deck
from models.player import Player
from views.playerview import PlayerView

MAX_PLAYERS_ALLOWED = 5


class GameController:
    def __init__(self, view: PlayerView) -> None:
        self.players = []
        self._deck: Deck = Deck()
        self._deck.shuffle()
        self.view = view
        self._players_hands = {}

    def register_player(self, player_name):
        if self.number_of_players_exceeded():
            current_player = Player(name=player_name)
            self.players.append(current_player)
            self._players_hands[current_player.id] = current_player._hand
        else:
            self.view.message = "Number of Players cannot exceed 5"

    def number_of_players_exceeded(self):
        return len(self.players) < MAX_PLAYERS_ALLOWED

    def register_players(self, players_name: List[Player]):
        for player_name in players_name:
            if self.number_of_players_exceeded():
                self.players.append(Player(name=player_name))
            else:
                self.view.message = "Number of Players cannot exceed 5"

    def get_a_player(self, index) -> Player:
        return self._players[index]

    def get_players(self) -> List[Player]:
        return self._players

    def get_players_hands(self):
        for player in self.players:
            self._players_hands[player.id] = player._hand
        return self._players_hands

    def give_a_card(self) -> None:
        cards = self._deck.get_cards()
        for player in self.players:
            player.add_a_card_in_hand(card=cards.pop())
            self._players_hands[player.id] = player._hand

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
