from views.playerview import PlayerView
from controllers.game_controller import GameController


def main():
    playerView = PlayerView()
    game = GameController(playerView)
    game.run()


if __name__ == "__main__":
    main()
