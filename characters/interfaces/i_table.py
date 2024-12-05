from abc import ABC, abstractmethod
from characters.models.player import Player
from typing import List

class ITable(ABC):
    @abstractmethod
    def add_player(self, player: Player) -> None:
        """Adiciona um jogador à mesa."""
        pass

    @abstractmethod
    def start_game(self) -> None:
        """Inicia o jogo."""
        pass

    @abstractmethod
    def next_turn(self) -> None:
        """Avança para o próximo turno."""
        pass

    @abstractmethod
    def get_winner(self) -> Player:
        """Retorna o jogador vencedor."""
        pass

    @abstractmethod
    def current_players(self) -> List[Player]:
        """Retorna a lista de jogadores atuais na mesa."""
        pass
