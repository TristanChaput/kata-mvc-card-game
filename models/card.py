class Card:
    _suit: str
    _rank: str
    _face_up: bool

    def __init__(self, suit: str, rank: str) -> None:
        self._suit: str = suit
        self._rank: str = rank
        self._face_up = False

    def __eq__(self, __o: object) -> bool:
        return self._suit == __o._suit and self._rank == __o._rank

    def is_turned_down(self) -> bool:
        return not self._face_up
