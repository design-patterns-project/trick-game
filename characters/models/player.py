from characters.interfaces.i_player import IPlayer

class Player(IPlayer):
    def __init__(self, name: str):
        self.name = name
        self.score = 0
        self.hand = []
        self.active = True
        self.mediator = None  # Inicialização da referência do Mediator

    def set_mediator(self, mediator):
        self.mediator = mediator  # Método para definir o mediador

    def play_card(self, card):
        if card in self.hand:
            self.hand.remove(card)
            print(f"{self.name} jogou a carta: {card}")
            self.complete_turn()  # Notificar que o turno foi concluído
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
