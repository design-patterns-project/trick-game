
from characters.interfaces.i_game import GameInterface
from characters.models.player import Player


class Game(GameInterface):
    def __init__(self, players: list[Player]):
        self.players = players
        self.winner = None
        self.current_turn = 0  # Index of the current player

    def start_game(self):
        print("Iniciando o jogo...")
        # Lógica para iniciar o jogo

    def end_game(self):
        print("Jogo terminado.")
        # Lógica para finalizar o jogo

    def get_winner(self):
        # Lógica para determinar o vencedor
        return self.winner

    def switch_turn(self):
        # Altera o turno para o próximo jogador
        self.current_turn = (self.current_turn + 1) % len(self.players)
        print(f"Turno mudado para {self.players[self.current_turn].name}")
