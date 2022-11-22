from views.view import IView


class PlayerView(IView):
    def player_register_name(self):
        name = input("player name : ")
        if not name:
            return None
        return name

    def show_player_hand(self, card):
        pass
