import random
from characters.interfaces.i_bot import IBot
from characters.models.card import Card
from characters.models.player import Player

class SimpleBot(Player, IBot):
    def __init__(self, name: str):
        super().__init__(name)
    
    def play_card(self) -> Card:
        if self.has_high_cards():
            return self.highest_card()
        else:
            return self.lowest_card()

    def request_truco(self) -> bool:
        return self.has_high_cards() and random.choice([True, False])

    def respond_to_truco(self) -> bool:
        return self.has_high_cards() or random.choice([True, False])

    def has_high_cards(self) -> bool:
        return any(card.value in ["3", "2", "manilha"] for card in self.hand)
    
    def highest_card(self) -> Card:
        return max(self.hand, key=lambda card: card.value)
    
    def lowest_card(self) -> Card:
        return min(self.hand, key=lambda card: card.value)
