from models.player import Player
from views.view import IView


class PlayerView(IView):
    def player_register_name(self):
        name = input("player name : ")
        if not name:
            return None
        return name

    def show_player_hand(self, player: Player):
        print(f"Player {player.get_name()}")
        if player.get_hand()[0].is_turned_down():
            print("face down card")
        else:
            print(player.get_hand()[0])
