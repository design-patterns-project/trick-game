from abc import ABC, abstractmethod

class PlayerProxyInterface(ABC):
    @abstractmethod
    def play_card(self, card):
        """Método para jogar uma carta."""
        pass
