from typing import List, Optional
import random
from characters.interfaces.i_bot import IBot
from characters.interfaces.i_game import GameInterface
from characters.models.bot import SimpleBot
from characters.models.player import Player
from designs_patterns.observer.interfaces.i_observer import IObserver
from designs_patterns.observer.interfaces.i_subject import ISubject
from designs_patterns.mediator.game_mediator import GameMediator
from characters.models.card import Card

class Game(GameInterface, ISubject):
    def __init__(self, players: List[Player], mediator: GameMediator):
        self.mediator = mediator
        self.players = players
        self.winner: Optional[str] = None
        self.current_turn: int = 0
        self.observers: List[IObserver] = []
        self.played_cards = []
        self.deck = self.create_deck()
        self.shuffle_deck()
        self.deal_cards()

    def create_deck(self):
        """Cria um baralho de cartas."""
        suits = ['Copas', 'Ouros', 'Espadas', 'Paus']
        values = ['A', '2', '3', '4', '5', '6', '7', 'Q', 'J', 'K']
        return [Card(value, suit) for suit in suits for value in values]

    def shuffle_deck(self):
        """Embaralha o baralho."""
        random.shuffle(self.deck)

    def deal_cards(self):
        """Distribui cartas aos jogadores."""
        for player in self.players:
            player.hand = self.draw_cards(3)

    def draw_cards(self, count: int) -> List[Card]:
        """Sorteia cartas do baralho."""
        drawn_cards = []
        for _ in range(count):
            if self.deck:
                drawn_cards.append(self.deck.pop())
        return drawn_cards

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
        self.play()

    def play(self):
        """Inicia o loop principal de interação do jogo no terminal."""
        while not self.winner:
            current_player = self.players[self.current_turn]
            print(f"Jogador atual: {current_player.name}")

            if isinstance(current_player, IBot):
                self.bot_turn(current_player)
            else:
                self.human_turn(current_player)

            self.check_winner()

    def human_turn(self, player: Player):
        """Menu de interação para o jogador humano realizar uma jogada."""
        print(f"\nÉ sua vez, {player.name}!")
        self.display_game_state(player)

        action = input("Escolha sua ação (1 - Jogar Carta, 2 - Gritar Truco, 3 - Desistir): ")

        if action == "1":
            self.play_card(player)
        elif action == "2":
            self.call_truco(player)
        elif action == "3":
            print(f"{player.name} desistiu do jogo.")
            self.winner = "Bots"
        else:
            print("Ação inválida. Tente novamente.")
            self.human_turn(player)

    def play_card(self, player: Player):
        """Permite que o jogador humano escolha uma carta para jogar."""
        print(f"\nEscolha uma carta para jogar, {player.name}. Sua mão: {[str(card) for card in player.hand]}")

        # Display player's hand with clear indices
        for i, card in enumerate(player.hand):
            print(f"{i + 1}: {card}")

        # Prompt for card selection
        while True:  # Loop until valid input is received
            try:
                choice = int(input("Escolha o número da carta: ")) - 1  # Convert to zero-based index

                if 0 <= choice < len(player.hand):
                    card = player.hand.pop(choice)  # Remove the card from hand
                    self.played_cards.append(card)  # Add the card to played cards
                    print(f"{player.name} jogou {card}\n")
                    self.notify(f"{player.name} jogou {card}.")
                    self.switch_turn()
                    break  # Exit loop if valid selection is made
                else:
                    print("Escolha inválida. Tente novamente.")
            except ValueError:
                print("Por favor, insira um número válido.")

    def bot_turn(self, bot: IBot):
        """Permite que o bot realize uma jogada automaticamente."""
        card = bot.play_card()
        self.played_cards.append(card)

        print(f"{bot.name} jogou {card.value} de {card.suit}")
        self.notify(f"{bot.name} jogou {card.value} de {card.suit}.")
        self.switch_turn()

    def display_game_state(self, player: Player):
        """Exibe o estado atual do jogo para o jogador humano."""
        print("\nCartas jogadas na mesa:")
        for card in self.played_cards:
            print(f"- {card}")

        print("\nSua mão:")
        for i, card in enumerate(player.hand, start=1):
            print(f"{i}: {card}")

        if self.played_cards:
            last_card = self.played_cards[-1]
            print(f"\nA carta a ser vencida é {last_card.value} de {last_card.suit}\n")

    def check_winner(self):
        """Verifica a condição de vitória e encerra o jogo."""
        if self.some_victory_condition():
            self.winner = self.players[self.current_turn].name
            print(f"O vencedor é {self.winner}!")
            self.end_game()

    def some_victory_condition(self):
        """Define a lógica para determinar se há um vencedor."""
        return any(len(player.hand) == 0 for player in self.players)

    def switch_turn(self):
        """Alterna para o próximo jogador."""
        self.current_turn = (self.current_turn + 1) % len(self.players)

    def end_game(self):
        """Encerra o jogo e notifica o resultado final."""
        print("Jogo encerrado!")
        self.notify("O jogo terminou!")

    def get_winner(self) -> Optional[str]:
        """Retorna o vencedor do jogo."""
        return self.winner

    def call_truco(self, player: Player):
        """Método para o jogador gritar truco de acordo com as regras do Truco Paulista."""
        print(f"\n{player.name} gritou TRUCO!")

        for opponent in self.players:
            if opponent != player:
                if isinstance(opponent, IBot): 
                    response = opponent.respond_to_truco()  

                    if response:
                        self.notify(f"{opponent.name} aceitou o truco!")
                        self.play()  
                        break  
                    else:
                        self.winner = player.name
                        print(f"{player.name} ganhou a rodada porque o adversário recusou o truco!")
                        self.end_game()
                        break  
                else:
                    response = random.choice([1, 2, 3])  
                    if response == 1:
                        self.notify(f"{opponent.name} aceitou o truco!")
                        self.play()
                        break
                    elif response == 2:
                        self.winner = player.name
                        print(f"{player.name} ganhou a rodada porque o adversário recusou o truco!")
                        self.end_game()
                        break
                    elif response == 3:
                        raise_ = random.choice([6, 9, 12])
                        self.notify(f"{opponent.name} aumentou a aposta para {raise_}!")
                        self.call_truco(player)
                        break
