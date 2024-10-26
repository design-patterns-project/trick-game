
from characters.interfaces.i_card import ICard


class Card(ICard):
    def __init__(self, value: str, suit: str):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} de {self.suit}"

    def compare(self, other):
        # Lógica para comparar cartas
        return self.value > other.value
