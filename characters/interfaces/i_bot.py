from abc import ABC, abstractmethod
from characters.models.card import Card

class IBot(ABC):
    @abstractmethod
    def name(self) -> str:
        """Nome do Bot."""
        pass

    @abstractmethod
    def play_card(self) -> Card:
        """Decide qual carta jogar."""
        pass

    @abstractmethod
    def request_truco(self) -> bool:
        """Decide se vai pedir truco."""
        pass

    @abstractmethod
    def respond_to_truco(self) -> bool:
        """Decide se vai aceitar ou recusar truco."""
        pass
