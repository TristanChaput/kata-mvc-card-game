from models.card import Card


def test_should_return_false_when_ace_of_spade_and_ace_of_club_are_compared():
    ace_of_spade = Card("♠", "A")
    ace_of_club = Card("♣", "A")

    assert ace_of_spade != ace_of_club


def test_should_return_true_when_two_ace_of_spade_are_compared():
    ace_of_spade_1 = Card("♠", "A")
    ace_of_spade_2 = Card("♠", "A")

    assert ace_of_spade_1 == ace_of_spade_2
