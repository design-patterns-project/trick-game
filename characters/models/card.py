from characters.interfaces.i_card import ICard

class Card(ICard):
    RANK_ORDER = {
        "4": 1, "5": 2, "6": 3, "7": 4, 
        "Q": 5, "J": 6, "K": 7, "A": 8, 
        "2": 9, "3": 10
    }  

    def __init__(self, value: str, suit: str):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} de {self.suit}"

    def compare(self, other):
        """Compara duas cartas com base no valor (rank)."""
        self_rank = Card.RANK_ORDER.get(self.value, 0)
        other_rank = Card.RANK_ORDER.get(other.value, 0)
        if self_rank > other_rank:
            return 1  
        elif self_rank < other_rank:
            return -1 
        else:
            return 0  
