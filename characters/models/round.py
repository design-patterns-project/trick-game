from typing import List

from characters.interfaces.i_round import IRound
from characters.models.player import Player

class Round(IRound):
    def __init__(self, players: List[Player]):
        self.players = players
        self.current_player_index = 0
        self.played_cards = []

    def start_round(self):
        print("Rodada iniciada.")

    def determine_winner(self):
        return self.players[0]  # Exemplo simplificado