from typing import Tuple


class Card:
    _suit: Tuple[int, str]
    _rank: Tuple[int, str]
    _face_up: bool

    def __init__(self, suit: Tuple[int, str], rank: Tuple[int, str]) -> None:
        self._suit: Tuple[int, str] = suit
        self._rank: Tuple[int, str] = rank
        self._face_up = False

    def __eq__(self, __o: object) -> bool:
        return (
            self.get_suit_weight() == __o.get_suit_weight()
            and self.get_rank_weight() == __o.get_rank_weight()
        )

    def flip(self) -> None:
        self._face_up = not self._face_up

    def get_rank_weight(self) -> int:
        return self._rank[0]

    def get_rank_symbol(self) -> str:
        return self._rank[1]

    def get_suit_weight(self) -> int:
        return self._suit[0]

    def get_suit_symbol(self) -> str:
        return self._suit[1]

    def is_turned_down(self) -> bool:
        return not self._face_up

    def __str__(self) -> str:
        return self.get_rank_symbol() + self.get_suit_symbol()
