from models.player import Player


def test_should_return_paul_when_player_name_paul_is_given():
    player = Player("Paul")

    expected = "Paul"
    player_name = player.get_name()

    assert player_name == expected
