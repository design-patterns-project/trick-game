from designs_patterns.mediator.interface.i_mediator import IMediator

class GameMediator(IMediator):
    def __init__(self):
        self.players = []

    def register_player(self, player):
        self.players.append(player)
        player.mediator = self  

    def notify(self, sender, event: str):
        if event == "turn_completed":
            print(f"{sender.name} terminou sua vez.")
            self.next_turn()

    def next_turn(self):
        print("É a vez do próximo jogador.")
