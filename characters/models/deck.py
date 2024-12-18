import random
from characters.interfaces.i_deck import IDeck
from characters.models.card import Card


class Deck(IDeck):
    def __init__(self):
        self.cards = [Card(value, suit) for value in ["A", "2", "3", "4", "5", "6", "7", "J", "Q", "K"] for suit in ["Copas", "Ouros", "Espadas", "Paus"]]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_cards(self, num_players: int, cards_per_player: int):
        """Distribui cartas para os jogadores."""
        hands = [[] for _ in range(num_players)]
        for _ in range(cards_per_player):
            for i in range(num_players):
                if self.cards:
                    hands[i].append(self.cards.pop())
        return hands
