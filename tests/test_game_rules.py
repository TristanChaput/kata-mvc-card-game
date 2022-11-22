import pytest
from controllers.game import Game
from models.card import Card

from models.player import Player
from views.playerview import PlayerView


@pytest.fixture
def paul():
    return Player(name="Paul")


@pytest.fixture
def pierre():
    return Player(name="Pierre")


@pytest.fixture
def playerview():
    return PlayerView()


@pytest.fixture
def game(playerview):
    return Game(view=playerview)


def test_should_return_paul_when_he_has_an_ace_and_pierre_has_a_king(
    monkeypatch, paul, game
):
    inputs = iter(["Paul", "Pierre"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr(Game, "MAX_PLAYERS_ALLOWED", 2)
    game.register_players()
    p1 = game.get_a_player(index=0)
    p2 = game.get_a_player(index=1)
    p1.add_a_card_in_hand(
        Card(
            (3, "♠"),
            (14, "A"),
        )
    )
    p2.add_a_card_in_hand(
        Card(
            (3, "♠"),
            (13, "K"),
        )
    )
    winner = game.check_for_a_winner()
    assert winner == paul


def test_should_return_jacques_when_he_has_an_ace_and_other_players_have_minor_ranks(
    monkeypatch, game
):
    inputs = iter(["Paul", "Pierre", "Hugues", "Tom", "Jacques"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    game.register_players()
    for player in game.get_players()[:4]:
        player.add_a_card_in_hand(
            Card(
                (3, "♠"),
                (13, "K"),
            )
        )
    p5 = game.get_a_player(index=4)
    p5.add_a_card_in_hand(
        Card(
            (3, "♠"),
            (14, "A"),
        )
    )
    winner = game.check_for_a_winner()
    jacques = Player("Jacques")
    assert winner == jacques


def test_should_return_jacques_when_he_has_an_ace_of_clubs_tom_and_ace_of_spades_and_other_players_have_minor_ranks_and_suits(
    monkeypatch, game
):
    inputs = iter(["Paul", "Pierre", "Hugues", "Tom", "Jacques"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    game.register_players()
    for player in game.get_players()[:3]:
        player.add_a_card_in_hand(
            Card(
                (3, "♠"),
                (13, "K"),
            )
        )
    p4 = game.get_a_player(index=3)
    p4.add_a_card_in_hand(
        Card(
            (3, "♠"),
            (14, "A"),
        )
    )
    p5 = game.get_a_player(index=4)
    p5.add_a_card_in_hand(
        Card(
            (4, "♣"),
            (14, "A"),
        )
    )
    winner = game.check_for_a_winner()
    jacques = Player("Jacques")
    assert winner == jacques
