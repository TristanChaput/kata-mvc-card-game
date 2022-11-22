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
            self._view.show_player_hand(player)

    def check_for_a_winner(self) -> Player:
        winner = self.get_a_player(index=0)
        for player in self._players[1:]:
            if self.winner_and_player_have_the_same_rank_but_winner_have_minor_suit(
                winner=winner,
                player=player,
            ) or self.winner_have_minor_rank_than_player(
                winner=winner,
                player=player,
            ):
                winner = player
        return winner

    def winner_and_player_have_the_same_rank_but_winner_have_minor_suit(
        self,
        winner,
        player,
    ) -> bool:
        if (
            winner.get_a_card_in_hand(index=0).get_rank_weight()
            == player.get_a_card_in_hand(index=0).get_rank_weight()
            and winner.get_a_card_in_hand(index=0).get_suit_weight()
            < player.get_a_card_in_hand(index=0).get_suit_weight()
        ):
            return True
        return False

    def winner_have_minor_rank_than_player(self, winner, player) -> bool:
        if (
            winner.get_a_card_in_hand(index=0).get_rank_weight()
            < player.get_a_card_in_hand(index=0).get_rank_weight()
        ):
            return True
        return False
