from typing import List
from models.player import Player


class Game:

    _players: List[Player]

    def __init__(self, players) -> None:
        if len(players) > 5:
            raise Exception("To many players")
        self._players = players

    def get_players(self) -> List[Player]:
        return self._players
