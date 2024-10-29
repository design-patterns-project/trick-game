from characters.interfaces.i_table import ITable
from characters.models.player import Player
from characters.models.card import Card
from typing import List

class Table(ITable):
    def __init__(self):
        self.players: List[Player] = []
        self.current_turn: int = 0

    def add_player(self, player: Player) -> None:
        if len(self.players) < 4:
            self.players.append(player)
            print(f"{player.name} foi adicionado à mesa.")
        else:
            print("A mesa já está cheia.")

    def start_game(self) -> None:
        if len(self.players) < 4:
            print("É necessário 4 jogadores para iniciar o jogo.")
            return
        print("O jogo começou!")
        self.deal_cards()
        self.current_turn = 0  # Inicia o turno

    def deal_cards(self) -> None:
        # Implementar a lógica de distribuição de cartas aqui
        print("Distribuindo cartas...")

    def next_turn(self) -> None:
        self.current_turn = (self.current_turn + 1) % len(self.players)
        current_player = self.players[self.current_turn]
        print(f"É a vez de {current_player.name}.")

    def get_winner(self) -> Player:
        # Implementar a lógica para determinar o vencedor do jogo
        pass

    def current_players(self) -> List[Player]:
        return self.players
