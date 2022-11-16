class Player:

    _name: str

    def __init__(self, name) -> None:
        self._name = name

    def get_name(self):
        return self._name
