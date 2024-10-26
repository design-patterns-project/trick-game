import random

from characters.interfaces.i_deck import IDeck
from characters.models.card import Card

class Deck(IDeck):
    def __init__(self):
        self.cards = [Card(value, suit) for value in ["A", "2", "3", "4", "5", "6", "7", "J", "Q", "K"] for suit in ["Copas", "Ouros", "Espadas", "Paus"]]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_cards(self):
        # Implementar lógica para distribuir cartas
        pass
