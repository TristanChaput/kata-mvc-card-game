from views.playerview import PlayerView
from controllers.game_controller import GameController
from models.player import Player
from models.card import Card, Rank, Suit
import pytest


def test_paul_should_have_a_card_in_hand():
    player_view = PlayerView()
    game_controller = GameController(view=player_view)
    paul = Player(name="Paul")
    game_controller.players.append(paul)

    game_controller.give_a_card()

    paul_hand = game_controller._players_hands[paul.id]
    assert paul_hand is not None


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
def test_all_players_should_face_up_their_cards(players, cards):
    player_view = PlayerView()
    game_controller = GameController(view=player_view)
    game_controller.players = players
    for i, player in enumerate(players):
        player.hand = [cards[i]]

    game_controller.show_cards()

    for player in game_controller.players:
        assert player.get_a_card_in_hand(index=0).face_up


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


# To refacto
def test_all_players_should_show_their_cards():
    pass


@pytest.mark.parametrize(
    "players",
    [
        (
            [
                Player(name="Paul"),
                Player(name="Pierre"),
            ]
        ),
        (
            [
                Player(name="David"),
                Player(name="Hugo"),
                Player(name="Gabin"),
                Player(name="Noam"),
            ]
        ),
    ],
    )
def test_each_player_should_have_a_card_but_not_the_same(players):
    player_view = PlayerView()
    game_controller = GameController(view=player_view)
    game_controller.players = players

    game_controller.give_a_card()

    cards = [player.hand[0] for player in game_controller.players]
    unordered_cards = set(cards)
    assert len(unordered_cards) == len(cards)


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

# def test_should_return_paul_when_he_has_an_ace_and_pierre_has_a_king(
#     monkeypatch, paul, game
# ):
#     inputs = iter(["Paul", "Pierre"])
#     monkeypatch.setattr("builtins.input", lambda _: next(inputs))
#     monkeypatch.setattr(GameController, "MAX_PLAYERS_ALLOWED", 2)
#     game.register_players()
#     p1 = game.get_a_player(index=0)
#     p2 = game.get_a_player(index=1)
#     p1.add_a_card_in_hand(
#         Card(
#             Suit(3, "♠"),
#             Rank(14, "A"),
#         )
#     )
#     p2.add_a_card_in_hand(
#         Card(
#             Suit(3, "♠"),
#             Rank(13, "K"),
#         )
#     )
#     winner = game.check_for_a_winner()
#     assert winner == paul

# To refacto
def test_should_return_jacques_when_he_has_an_ace_and_other_players_have_minor_ranks(
    monkeypatch, game
):
    inputs = iter(["Paul", "Pierre", "Hugues", "Tom", "Jacques"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    game.register_players()
    for player in game.players[:4]:
        player.add_a_card_in_hand(
            Card(
                Suit(3, "♠"),
                Rank(13, "K"),
            )
        )
    p5 = game.get_a_player(index=4)
    p5.add_a_card_in_hand(
        Card(
            Suit(3, "♠"),
            Rank(14, "A"),
        )
    )
    winner = game.check_for_a_winner()
    jacques = Player("Jacques")
    assert winner == jacques


# To refacto
def test_should_return_jacques_when_he_has_an_ace_of_clubs_tom_and_ace_of_spades_and_other_players_have_minor_ranks_and_suits(
    monkeypatch, game
):
    inputs = iter(["Paul", "Pierre", "Hugues", "Tom", "Jacques"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    game.register_players()
    for player in game.players[:3]:
        player.add_a_card_in_hand(
            Card(
                Suit(3, "♠"),
                Rank(13, "K"),
            )
        )
    p4 = game.get_a_player(index=3)
    p4.add_a_card_in_hand(
        Card(
            Suit(3, "♠"),
            Rank(14, "A"),
        )
    )
    p5 = game.get_a_player(index=4)
    p5.add_a_card_in_hand(
        Card(
            Suit(4, "♣"),
            Rank(14, "A"),
        )
    )
    winner = game.check_for_a_winner()
    jacques = Player("Jacques")
    assert winner == jacques


def test_should_show_jacques_when_he_has_an_ace_of_clubs_tom_and_ace_of_spades_and_other_players_have_minor_ranks_and_suits(
    capsys, monkeypatch, game, playerview
):
    inputs = iter(["Paul", "Pierre", "Hugues", "Tom", "Jacques"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    game.register_players()
    for player in game.players[:3]:
        player.add_a_card_in_hand(
            Card(
                Suit(3, "♠"),
                Rank(13, "K"),
            )
        )
    p4 = game.get_a_player(index=3)
    p4.add_a_card_in_hand(
        Card(
            Suit(3, "♠"),
            Rank(14, "A"),
        )
    )
    p5 = game.get_a_player(index=4)
    p5.add_a_card_in_hand(
        Card(
            Suit(4, "♣"),
            Rank(14, "A"),
        )
    )
    winner = game.check_for_a_winner()
    playerview.show_winner(winner)
    out, err = capsys.readouterr()
    expected = "The winner is Jacques, with a A♣\n"
    assert out == expected


# To refacto
def test_should_return_pierre_when_others_players_have_minor_ranks_and_suits(
    capsys, monkeypatch, game
):
    inputs = iter(["Paul", "Pierre", "Hugues", "Tom", "Jacques"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    game.register_players()

    paul = game.get_a_player(index=0)
    pierre = game.get_a_player(index=1)
    hugues = game.get_a_player(index=2)
    tom = game.get_a_player(index=3)
    jacques = game.get_a_player(index=4)

    paul.add_a_card_in_hand(
        Card(
            Suit(1, "♦"),
            Rank(13, "K"),
        )
    )
    pierre.add_a_card_in_hand(
        Card(
            Suit(3, "♠"),
            Rank(13, "K"),
        )
    )
    hugues.add_a_card_in_hand(
        Card(
            Suit(1, "♦"),
            Rank(6, "6"),
        )
    )
    tom.add_a_card_in_hand(
        Card(
            Suit(3, "♠"),
            Rank(10, "10"),
        )
    )
    jacques.add_a_card_in_hand(
        Card(
            Suit(1, "♦"),
            Rank(8, "8"),
        )
    )

    winner = game.check_for_a_winner()

    expected_player = Player("Pierre")
    game._view.show_winner(winner)

    out, err = capsys.readouterr()
    expected = "The winner is Pierre, with a K♠\n"
    assert winner == expected_player
    assert out == expected
