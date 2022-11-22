from views.playerview import PlayerView
from controllers.game import Game


def main():
    playerView = PlayerView()
    game = Game(playerView)
    game.run()


if __name__ == "__main__":
    main()
