from controllers.game_controller import GameController
from models.card import Card, Rank, Suit
from models.player import Player
import pytest

from views.playerview import PlayerView


@pytest.fixture
def playerview():
    return PlayerView()


@pytest.fixture
def game(playerview):
    return GameController(view=playerview)


# def test_paul_should_be_registered(monkeypatch, game):
#     monkeypatch.setattr("builtins.input", lambda _: "Paul")
#     monkeypatch.setattr(GameController, "MAX_PLAYERS_ALLOWED", 1)

#     game.register_players()

#     player = game.get_a_player(index=0)
#     assert player.name == "Paul"


# def test_should_return_players_when_a_game_with_players_is_created(
#     monkeypatch, game, paul, pierre
# ):
#     inputs = iter(["Paul", "Pierre"])
#     monkeypatch.setattr("builtins.input", lambda _: next(inputs))
#     monkeypatch.setattr(GameController, "MAX_PLAYERS_ALLOWED", 2)

#     game.register_players()

#     players = game.players
#     expected = [paul, pierre]
#     assert players == expected


def test_should_return_five_players_when_a_game_with_more_than_five_players_is_created(
    monkeypatch, game, paul, pierre, hugues, tom, jacques
):
    inputs = iter(["Paul", "Pierre", "Hugues", "Tom", "Jacques", "Lea"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    game.register_players()

    players = game.players
    expected = [paul, pierre, hugues, tom, jacques]
    assert players == expected


def test_paul_should_have_a_card_in_hand():
    player_view = PlayerView()
    game_controller = GameController(view=player_view)
    paul = Player(name="Paul")
    game_controller.players.append(paul)

    game_controller.give_a_card()

    paul_hand = game_controller._players_hands[paul.id]
    assert paul_hand is not None


# def test_paul_and_pierre_should_have_a_card_but_not_the_same(monkeypatch, game):
#     inputs = iter(["Paul", "Pierre"])
#     monkeypatch.setattr("builtins.input", lambda _: next(inputs))
#     monkeypatch.setattr(GameController, "MAX_PLAYERS_ALLOWED", 2)
#     game.register_players()
#     game.give_a_card()
#     paul_hand = game.get_a_player(index=0).get_a_card_in_hand(index=0)
#     pierre_hand = game.get_a_player(index=1).get_a_card_in_hand(index=0)
#     assert paul_hand != pierre_hand


# def test_paul_should_have_a_card_with_face_down(monkeypatch, game):
#     monkeypatch.setattr("builtins.input", lambda _: "Paul")
#     monkeypatch.setattr(GameController, "MAX_PLAYERS_ALLOWED", 1)
#     game.register_players()
#     game.give_a_card()
#     paul_hand = game.get_a_player(index=0).get_a_card_in_hand(index=0)
#     assert paul_hand.is_turned_down()


# def test_should_flip_paul_hand_with_face_up(monkeypatch, game):
#     monkeypatch.setattr("builtins.input", lambda _: "Paul")
#     monkeypatch.setattr(GameController, "MAX_PLAYERS_ALLOWED", 1)
#     game.register_players()
#     game.give_a_card()
#     paul = game.get_a_player(index=0)
#     paul.flip_hand()
#     paul_hand = game.get_a_player(index=0).get_a_card_in_hand(index=0)
#     assert not paul_hand.is_turned_down()


def test_should_view_paul_hand_with_face_up(capsys, playerview, paul):
    paul.add_a_card_in_hand(
        Card(
            Suit(3, "♠"),
            Rank(14, "A"),
        )
    )
    paul.flip_hand()

    playerview.show_player_hand(paul)

    out, err = capsys.readouterr()
    expected = "Player Paul\nA♠\n"
    assert out == expected


def test_should_view_paul_hand_with_face_down(capsys, playerview, paul):
    paul.add_a_card_in_hand(Card((3, "♠"), (14, "A")))
    playerview.show_player_hand(paul)
    out, err = capsys.readouterr()
    expected = "Player Paul\nface down card\n"
    assert out == expected


def test_all_players_should_face_up_their_cards(monkeypatch, game):
    inputs = iter(["Paul", "Pierre", "Hugues", "Tom", "Jacques"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    game.register_players()
    game.give_a_card()

    game.show_cards()

    players = game.players
    for player in players:
        assert not player.get_a_card_in_hand(index=0).is_turned_down()


def test_all_players_should_show_their_cards(capsys, monkeypatch, game):
    inputs = iter(["Paul", "Pierre", "Hugues", "Tom", "Jacques"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    game.register_players()
    players = game.players
    for player in players:
        player.add_a_card_in_hand(
            Card(
                Suit(3, "♠"),
                Rank(14, "A"),
            )
        )

    game.show_cards()

    out, err = capsys.readouterr()
    expected = (
        "Player Paul\nA♠\n"
        "Player Pierre\nA♠\n"
        "Player Hugues\nA♠\n"
        "Player Tom\nA♠\n"
        "Player Jacques\nA♠\n"
    )
    assert out == expected


@pytest.mark.parametrize(
    "players, cards",
    [
        (
            [
                Player(name="Paul"),
                Player(name="Pierre"),
            ],
            [
                Card(Suit(1, "♦"), Rank(2, "2")),
                Card(Suit(1, "♦"), Rank(3, "3")),
            ],
        ),
        (
            [
                Player(name="Philippe"),
                Player(name="Pascal"),
                Player(name="Hugo"),
            ],
            [
                Card(Suit(1, "♦"), Rank(2, "2")),
                Card(Suit(1, "♦"), Rank(3, "3")),
                Card(Suit(1, "♦"), Rank(4, "4")),
            ],
        ),
    ],
)
def test_should_return_players_hand_with_player_id(players, cards):
    player_view = PlayerView()
    game_controller = GameController(view=player_view)
    for i, player in enumerate(players):
        player.hand = [cards[i]]

    game_controller.players = players

    players_hands = game_controller.get_players_hands()

    expected_players_hands = {}
    for i, player in enumerate(players):
        expected_players_hands[player.id] = [cards[i]]
    assert players_hands == expected_players_hands


@pytest.mark.parametrize(
    "players",
    [
        (["Paul", "Pierre", "Hugues", "Tom", "Jacques", "Léa"]),
        (["Philippe", "Pascal", "Hugo", "Tommy", "Jack", "Mark", "Lisa"]),
    ],
)
def test_game_should_not_exceed_five_players(players):
    player_view = PlayerView()
    game_controller = GameController(view=player_view)
    expected_message = "Number of Players cannot exceed 5"

    for player in players:
        game_controller.register_player(player)

    expected_players = [Player(name=player_name) for player_name in players[:5]]
    assert game_controller.players == expected_players
    assert game_controller.view.message == expected_message


@pytest.mark.parametrize(
    "players, message",
    [
        (["Paul", "Pierre", "Hugues"], ""),
        (["Philippe", "Pascal", "Hugo", "Tommy"], ""),
        (
            ["Philippe", "Pascal", "Hugo", "Tommy", "Jack", "Mark", "Lisa"],
            "Number of Players cannot exceed 5",
        ),
    ],
)
def test_game_should_register_multiple_players(players, message):
    player_view = PlayerView()
    game_controller = GameController(view=player_view)
    expected_message = message

    game_controller.register_players(players)

    expected_players = [Player(name=player_name) for player_name in players[:5]]
    assert game_controller.players == expected_players
    assert game_controller.view.message == expected_message
