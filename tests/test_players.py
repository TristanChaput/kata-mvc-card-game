from controllers.game import Game
from models.player import Player
import pytest


@pytest.fixture
def paul():
    return Player("Paul")


@pytest.fixture
def pierre():
    return Player("Pierre")


@pytest.fixture
def tom():
    return Player("Tom")


@pytest.fixture
def jacques():
    return Player("Jacques")


@pytest.fixture
def hugues():
    return Player("Hugues")


@pytest.fixture
def lea():
    return Player("Lea")


def test_should_return_paul_when_player_name_paul_is_given():
    player = Player("Paul")

    expected = "Paul"
    player_name = player.get_name()

    assert player_name == expected


def test_should_return_players_when_a_game_with_players_is_created(paul, pierre):
    game = Game([paul, pierre])

    players = game.get_players()
    expected = [paul, pierre]

    assert players == expected


def test_should_throw_an_exception_when_a_game_with_more_than_five_players_is_created(
    paul, pierre, hugues, tom, jacques, lea
):
    with pytest.raises(Exception):
        Game([paul, pierre, hugues, tom, jacques, lea])
