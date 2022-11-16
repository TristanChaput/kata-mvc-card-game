import pytest
from models.card import Card
from models.deck import Deck


@pytest.fixture
def suits():
    return [
        "♠",
        "♣",
        "♥",
        "♦",
    ]


@pytest.fixture
def ranks():
    return [
        "A",
        "K",
        "Q",
        "J",
        "10",
        "9",
        "8",
        "7",
        "6",
        "5",
        "4",
        "3",
        "2",
    ]


@pytest.fixture
def list_of_52_cards(suits, ranks):
    cards = []
    for suit in suits:
        for rank in ranks:
            cards.append(Card(suit, rank))
    return cards


def test_should_return_false_when_ace_of_spade_and_ace_of_club_are_compared():
    ace_of_spade = Card("♠", "A")
    ace_of_club = Card("♣", "A")

    assert ace_of_spade != ace_of_club


def test_should_return_true_when_two_ace_of_spade_are_compared():
    ace_of_spade_1 = Card("♠", "A")
    ace_of_spade_2 = Card("♠", "A")

    assert ace_of_spade_1 == ace_of_spade_2


def test_should_return_deck_of_52_cards(list_of_52_cards):
    deck = Deck()
    expected = list_of_52_cards

    cards = deck.get_cards()

    assert cards == expected
