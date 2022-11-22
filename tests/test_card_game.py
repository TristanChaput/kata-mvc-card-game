import pytest
from models.card import Card
from models.deck import Deck


@pytest.fixture
def suits():
    return {
        1: "♦",
        2: "♥",
        3: "♠",
        4: "♣",
    }


@pytest.fixture
def ranks():
    return {
        14: "A",
        13: "K",
        12: "Q",
        11: "J",
        10: "10",
        9: "9",
        8: "8",
        7: "7",
        6: "6",
        5: "5",
        4: "4",
        3: "3",
        2: "2",
    }


@pytest.fixture
def list_of_52_cards(suits, ranks):
    cards = []
    for weight, suit in suits.items():
        for weight, rank in ranks.items():
            cards.append(
                Card(
                    (weight, suit),
                    (weight, rank),
                )
            )
    return cards


def test_should_return_false_when_ace_of_spade_and_ace_of_club_are_compared():
    ace_of_spade = Card((3, "♠"), (14, "A"))
    ace_of_club = Card((4, "♣"), (14, "A"))

    assert ace_of_spade != ace_of_club


def test_should_return_true_when_two_ace_of_spade_are_compared():
    ace_of_spade_1 = Card((3, "♠"), (14, "A"))
    ace_of_spade_2 = Card((3, "♠"), (14, "A"))

    assert ace_of_spade_1 == ace_of_spade_2


def test_should_return_deck_of_52_cards(list_of_52_cards):
    deck = Deck()
    expected = list_of_52_cards

    cards = deck.get_cards()

    assert cards == expected


def test_should_return_a_deck_of_52_cards_in_different_order(list_of_52_cards):
    deck = Deck()
    expected_ordered_list = list_of_52_cards
    expected_length = 52

    deck.shuffle()

    cards = deck.get_cards()

    assert len(cards) == expected_length
    assert cards != expected_ordered_list


def test_should_return_flipped_card():
    ace_of_spade = Card((3, "♠"), (14, "A"))
    ace_of_spade.flip()
    assert not ace_of_spade.is_turned_down()
