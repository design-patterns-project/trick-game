from characters.interfaces.i_player import IPlayer


class Player(IPlayer):
    def __init__(self, name: str):
        self.name = name
        self.score = 0
        self.hand = []
        self.active = True

    def play_card(self, card):
        if card in self.hand:
            self.hand.remove(card)
            print(f"{self.name} jogou a carta: {card}")
        else:
            print("Carta não está na mão.")

    def call_truco(self):
        print(f"{self.name} gritou truco!")

    def accept_truco(self):
        print(f"{self.name} aceitou o truco.")

    def refuse_truco(self):
        print(f"{self.name} recusou o truco.")
