from typing import List
from characters.interfaces.i_game import GameInterface
from characters.models.player import Player
from designs_patterns.observer.interfaces.i_observer import IObserver
from designs_patterns.observer.interfaces.i_subject import ISubject

class Game(GameInterface, ISubject):
    def __init__(self, players: List[Player], mediator):
        self.players = players
        self.winner = None  
        self.current_turn = 0  
        self.mediator = mediator  
        self.observers: List[IObserver] = []  

    def attach(self, observer: IObserver):
        """Adiciona um observador à lista."""
        self.observers.append(observer)

    def detach(self, observer: IObserver):
        """Remove um observador da lista."""
        self.observers.remove(observer)

    def notify(self, message: str):
        """Notifica todos os observadores sobre um evento."""
        for observer in self.observers:
            observer.update(message)

    def start_game(self):
        print("Iniciando o jogo...")
        self.notify("O jogo começou!")  
        # Lógica para iniciar o jogo

    def end_game(self):
        print("Jogo terminado.")
        self.notify("O jogo terminou.")  
        # Lógica para finalizar o jogo

    def get_winner(self):
        # Lógica para determinar o vencedor
        return self.winner

    def switch_turn(self):
        # Altera o turno para o próximo jogador
        self.current_turn = (self.current_turn + 1) % len(self.players)
        print(f"Turno mudado para {self.players[self.current_turn].name}")
        self.notify(f"Turno mudado para {self.players[self.current_turn].name}.")  
        
        # Notificar o mediador sobre a mudança de turno, se necessário
        if self.mediator:
            self.mediator.notify(self.players[self.current_turn], "turn_started")

    def is_player_turn(self, player: Player) -> bool:
        """Verifica se é a vez do jogador."""
        return self.players[self.current_turn] == player
