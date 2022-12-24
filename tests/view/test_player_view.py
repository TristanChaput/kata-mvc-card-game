from views.playerview import PlayerView
from controllers.game_controller import GameController
from models.player import Player
from models.card import Card, Rank, Suit
import pytest


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
