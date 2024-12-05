import random
from characters.interfaces.i_bot import IBot
from characters.models.card import Card
from characters.models.player import Player

class SimpleBot(Player, IBot):
    def __init__(self, name: str):
        super().__init__(name)
    
    def play_card(self) -> Card:
        """Escolhe uma carta para jogar com base nas cartas que o bot tem."""
        if self.has_high_cards():
            return self.highest_card()
        else:
            return self.lowest_card()

    def request_truco(self) -> bool:
        """Decide se o bot vai gritar truco ou não com base nas cartas que possui."""
        return self.has_high_cards() and random.choice([True, False])

    def respond_to_truco(self) -> bool:
        """Decide se o bot vai aceitar ou recusar um truco gritado com base na sua mão e um fator de chance."""
        if self.has_high_cards():
            return random.random() < 0.75  
        else:
            return random.random() < 0.25  

    def has_high_cards(self) -> bool:
        """Verifica se o bot possui cartas altas (3, 2 ou manilha)."""
        return any(card.value in ["3", "2", "manilha"] for card in self.hand)
    
    def highest_card(self) -> Card:
        """Retorna a carta de maior valor que o bot tem na mão."""
        return max(self.hand, key=lambda card: card.value)
    
    def lowest_card(self) -> Card:
        """Retorna a carta de menor valor que o bot tem na mão."""
        return min(self.hand, key=lambda card: card.value)
