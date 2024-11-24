from characters.interfaces.i_player import IPlayer

class Player(IPlayer):
    def __init__(self, name: str):
        self._name = name  
        self.score = 0
        self.hand = []
        self.active = True
        self.mediator = None  

    @property
    def name(self) -> str:
        return self._name  

    def set_mediator(self, mediator):
        self.mediator = mediator  

    def play_card(self, card):
        """Método para jogar uma carta, chamado quando o jogador humano decide jogar uma carta."""
        if card in self.hand:
            self.hand.remove(card)
            print(f"{self.name} jogou a carta: {card}")
            self.complete_turn()  
        else:
            print("Carta não está na mão.")

    def complete_turn(self):
        """Finaliza o turno do jogador e notifica o mediador."""
        print(f"{self.name} completou seu turno.")
        if self.mediator:
            self.mediator.notify(self, "turn_completed")

    def call_truco(self):
        """Método para gritar truco, chamado quando o jogador deseja gritar truco."""
        print(f"{self.name} gritou truco!")

    def accept_truco(self):
        """Aceita o truco quando o jogador decide aceitar."""
        print(f"{self.name} aceitou o truco.")

    def refuse_truco(self):
        """Recusa o truco quando o jogador decide recusar."""
        print(f"{self.name} recusou o truco.")

    def has_card(self, card):
        """Verifica se o jogador possui a carta em sua mão."""
        return card in self.hand
