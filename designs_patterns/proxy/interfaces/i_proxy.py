from abc import ABC, abstractmethod
from characters.models.card import Card

class IPlayerProxy(ABC):
    @abstractmethod
    def play_card(self, card: Card) -> None:
        pass
