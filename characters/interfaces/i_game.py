from abc import ABC, abstractmethod

class GameInterface(ABC):
    @abstractmethod
    def start_game(self):
        """Método para iniciar o jogo."""
        pass

    @abstractmethod
    def end_game(self):
        """Método para encerrar o jogo."""
        pass

    @abstractmethod
    def get_winner(self):
        """Método para obter o vencedor do jogo."""
        pass

    @abstractmethod
    def switch_turn(self):
        pass
