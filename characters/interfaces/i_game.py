from abc import ABC, abstractmethod
from typing import List
from characters.models.card import Card
from characters.models.player import Player

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
    def get_winner(self) -> str:
        """Método para obter o vencedor do jogo."""
        pass

    @abstractmethod
    def switch_turn(self):
        """Alterna para o próximo jogador."""
        pass

    @abstractmethod
    def play_card(self, player: Player, card: Card):
        """Método para o jogador jogar uma carta."""
        pass

    @abstractmethod
    def call_truco(self, player: Player):
        """Método para o jogador gritar truco."""
        pass

    @abstractmethod
    def check_winner(self) -> bool:
        """Método para verificar se há um vencedor."""
        pass

    @abstractmethod
    def display_game_state(self, player: Player):
        """Exibe o estado atual do jogo para o jogador."""
        pass
