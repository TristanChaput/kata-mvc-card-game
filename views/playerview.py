from models.player import Player


class PlayerView:
    def __init__(self) -> None:
        super().__init__()
        self.message = ""

    def player_register_name(self):
        name = input("player name : ")
        if not name:
            return None
        return name

    def show_player_hand(self, player: Player):
        print(f"Player {player.name}")
        if player.get_a_card_in_hand(index=0).is_turned_down():
            print("face down card")
        else:
            print(player.get_a_card_in_hand(index=0))

    def show_winner(self, player: Player):
        print(
            f"The winner is {player.name}, with a {player.get_a_card_in_hand(index=0)}"
        )
