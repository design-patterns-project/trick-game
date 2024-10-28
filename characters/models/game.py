from typing import List
from characters.interfaces.i_game import GameInterface
from characters.models.player import Player
from designs_patterns.observer.interfaces.i_observer import IObserver
from designs_patterns.observer.interfaces.i_subject import ISubject
from designs_patterns.proxy.player_proxy import PlayerProxy


class Game(GameInterface, ISubject):
    def __init__(self, players: List[Player], mediator):
        self.players = players
        self.winner = None  
        self.current_turn = 0  
        self.mediator = mediator  
        self.observers: List[IObserver] = []  
        # Cria proxies para cada jogador
        self.player_proxies = [PlayerProxy(player, self) for player in players]

    def attach(self, observer: IObserver):
        self.observers.append(observer)

    def detach(self, observer: IObserver):
        self.observers.remove(observer)

    def notify(self, message: str):
        for observer in self.observers:
            observer.update(message)

    def start_game(self):
        print("Iniciando o jogo...")
        self.notify("O jogo começou!")

    def end_game(self):
        print("Jogo terminado.")
        self.notify("O jogo terminou.")

    def get_winner(self):
        return self.winner

    def switch_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.players)
        print(f"Turno mudado para {self.players[self.current_turn].name}")
        self.notify(f"Turno mudado para {self.players[self.current_turn].name}.")
        if self.mediator:
            self.mediator.notify(self.players[self.current_turn], "turn_started")

    def is_player_turn(self, player: Player) -> bool:
        return self.players[self.current_turn] == player

    def get_player_proxy(self, player: Player) -> PlayerProxy:
        for proxy in self.player_proxies:
            if proxy.player == player:
                return proxy
        raise ValueError("Jogador não encontrado.")
