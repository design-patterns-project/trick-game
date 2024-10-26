from characters.interfaces.i_player import IPlayer

class Player(IPlayer):
    def __init__(self, name: str):
        self.name = name
        self.score = 0
        self.hand = []
        self.active = True
        self.mediator = None  

    def set_mediator(self, mediator):
        self.mediator = mediator  

    def play_card(self, card):
        if card in self.hand:
            self.hand.remove(card)
            print(f"{self.name} jogou a carta: {card}")
            self.complete_turn()  
        else:
            print("Carta não está na mão.")

    def complete_turn(self):
        print(f"{self.name} completou seu turno.")
        if self.mediator:
            self.mediator.notify(self, "turn_completed")

    def call_truco(self):
        print(f"{self.name} gritou truco!")

    def accept_truco(self):
        print(f"{self.name} aceitou o truco.")

    def refuse_truco(self):
        print(f"{self.name} recusou o truco.")

    def has_card(self, card):
        """Verifica se o jogador possui a carta em sua mão."""
        return card in self.hand
