from typing import List

from characters.interfaces.i_hand import IHand
from characters.models.card import Card

class Hand(IHand):
    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def remove_card(self, card: Card):
        self.cards.remove(card)

    def calculate_points(self):
        return len(self.cards)  
