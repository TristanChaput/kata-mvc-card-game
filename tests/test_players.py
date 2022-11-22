from controllers.game import Game
from models.player import Player
import pytest

from views.playerview import PlayerView


@pytest.fixture
def paul():
    return Player(name="Paul")


@pytest.fixture
def pierre():
    return Player(name="Pierre")


@pytest.fixture
def tom():
    return Player(name="Tom")


@pytest.fixture
def jacques():
    return Player(name="Jacques")


@pytest.fixture
def hugues():
    return Player(name="Hugues")


@pytest.fixture
def playerview():
    return PlayerView()


@pytest.fixture
def game(playerview):
    return Game(view=playerview)


def test_should_return_paul_when_player_name_paul_is_given():
    player = Player("Paul")

    expected = "Paul"
    player_name = player.get_name()

    assert player_name == expected


def test_paul_should_be_registered(monkeypatch, game):
    monkeypatch.setattr("builtins.input", lambda _: "Paul")
    monkeypatch.setattr(Game, "MAX_PLAYERS_ALLOWED", 1)
    game.register_players()
    player = game.get_a_player(index=0)
    assert player.get_name() == "Paul"


def test_should_return_players_when_a_game_with_players_is_created(
    monkeypatch, game, paul, pierre
):
    inputs = iter(["Paul", "Pierre"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr(Game, "MAX_PLAYERS_ALLOWED", 2)
    game.register_players()
    players = game.get_players()
    expected = [paul, pierre]
    assert players == expected


def test_should_return_five_players_when_a_game_with_more_than_five_players_is_created(
    monkeypatch, game, paul, pierre, hugues, tom, jacques
):
    inputs = iter(["Paul", "Pierre", "Hugues", "Tom", "Jacques", "Lea"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    game.register_players()
    players = game.get_players()
    expected = [paul, pierre, hugues, tom, jacques]
    assert players == expected


def test_paul_should_have_a_card(monkeypatch, game):
    monkeypatch.setattr("builtins.input", lambda _: "Paul")
    monkeypatch.setattr(Game, "MAX_PLAYERS_ALLOWED", 1)
    game.register_players()
    game.give_a_card()
    paul_hand = game.get_a_player(index=0).get_hand()
    assert len(paul_hand) == 1


def test_paul_and_pierre_should_have_a_card_but_not_the_same(monkeypatch, game):
    inputs = iter(["Paul", "Pierre"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr(Game, "MAX_PLAYERS_ALLOWED", 2)
    game.register_players()
    game.give_a_card()
    paul_hand = game.get_a_player(index=0).get_hand()
    pierre_hand = game.get_a_player(index=1).get_hand()
    assert len(paul_hand) == 1
    assert len(pierre_hand) == 1
    assert paul_hand != pierre_hand


def test_paul_should_have_a_card_with_face_down(monkeypatch, game):
    monkeypatch.setattr("builtins.input", lambda _: "Paul")
    monkeypatch.setattr(Game, "MAX_PLAYERS_ALLOWED", 1)
    game.register_players()
    game.give_a_card()
    paul_hand = game.get_a_player(index=0).get_hand()
    assert paul_hand[0].is_turned_down()
