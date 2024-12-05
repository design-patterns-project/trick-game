from typing import List
from characters.models.player import Player
from characters.models.bot import SimpleBot
from designs_patterns.mediator.interface.i_mediator import IMediator

class GameMediator(IMediator):
    def __init__(self):
        self.players: List[Player] = []
        self.current_turn: int = 0
        self.truco_called: bool = False
        self.played_cards = []
        self.scores = {}  # Dicionário para armazenar as pontuações dos jogadores
        self.max_points = 12  # Pontuação necessária para vencer

    def register_player(self, player: Player):
        """Registra um jogador no mediador."""
        self.players.append(player)
        player.mediator = self
        self.scores[player.name] = 0  # Inicializa a pontuação do jogador

    def notify(self, sender, event: str):
        """Notifica o mediador sobre eventos que ocorrem durante o jogo."""
        if event == "turn_completed":
            print(f"{sender.name} terminou sua vez.")
            self.next_turn()
        elif event == "call_truco":
            self.handle_truco(sender)
        elif event == "card_played":
            self.handle_card_played(sender)

    def next_turn(self):
        """Alterna para o próximo jogador e verifica se é hora de terminar o jogo."""
        self.current_turn = (self.current_turn + 1) % len(self.players)
        current_player = self.players[self.current_turn]
        print(f"\nÉ a vez de {current_player.name} agora.")
        
        if isinstance(current_player, SimpleBot):
            self.bot_turn(current_player)
        else:
            self.human_turn(current_player)

    def handle_truco(self, sender: Player):
        """Gerencia quando um jogador ou bot grita truco."""
        print(f"{sender.name} gritou truco!")

        for player in self.players:
            if player != sender:
                self.respond_to_truco(player)

    def respond_to_truco(self, player: Player):
        """Simula a resposta de um jogador ao truco gritado."""
        if isinstance(player, SimpleBot):
            self.bot_respond_to_truco(player)
        else:
            print(f"{player.name}, você foi chamado para responder ao truco!")
            action = input("Escolha sua resposta (1 - Aceitar, 2 - Recusar): ")
            if action == "1":
                print(f"{player.name} aceitou o truco!")
                self.update_score(player, 1)  # Exemplo de atualização de pontos
            else:
                print(f"{player.name} recusou o truco.")
                self.update_score(player, -1)

    def bot_respond_to_truco(self, bot: SimpleBot):
        """Lógica do bot para responder ao truco."""
        print(f"{bot.name} decidiu aceitar o truco automaticamente.")
        self.update_score(bot, 1)  # Exemplo de atualização de pontos

    def human_turn(self, player: Player):
        """Gerencia a vez do jogador humano."""
        print(f"\nÉ sua vez, {player.name}!")
        self.display_game_state(player)

        action = input("Escolha sua ação (1 - Jogar Carta, 2 - Gritar Truco, 3 - Desistir): ")

        if action == "1":
            self.play_card(player)
        elif action == "2":
            self.call_truco(player)
        elif action == "3":
            print(f"{player.name} desistiu do jogo.")
            self.end_game(player)
        else:
            print("Ação inválida. Tente novamente.")
            self.human_turn(player)

    def play_card(self, player: Player):
        """Método para jogar uma carta, chamado pelo jogador humano."""
        print(f"{player.name}, você escolheu jogar uma carta.")
        self.played_cards.append(player.hand.pop())  # Remover uma carta da mão do jogador
        self.notify(player, "card_played")

    def call_truco(self, player: Player):
        """Método para gritar truco, chamado pelo jogador humano."""
        self.notify(player, "call_truco")

    def display_game_state(self, player: Player):
        """Exibe o estado atual do jogo para o jogador humano."""
        print(f"\nCartas jogadas até agora: ")
        for card in self.played_cards:
            print(f"- {card}")

        print(f"\nSua mão: ")
        for i, card in enumerate(player.hand):
            print(f"{i + 1}: {card}")

    def end_game(self, player: Player):
        """Encerra o jogo."""
        print(f"O jogo terminou! {player.name} perdeu.")
        self.notify(player, "game_over")

    def update_score(self, player: Player, points: int):
        """Atualiza a pontuação do jogador."""
        self.scores[player.name] += points
        print(f"{player.name} agora tem {self.scores[player.name]} pontos.")

        # Verifica se algum jogador alcançou a pontuação máxima
        if self.scores[player.name] >= self.max_points:
            print(f"\n{player.name} venceu o jogo com {self.scores[player.name]} pontos!")
            self.end_game(player)

    def handle_card_played(self, sender: Player):
        """Lida com as cartas jogadas por jogadores e calcula a pontuação da rodada."""
        print(f"{sender.name} jogou uma carta.")
        
        # Verifica as cartas jogadas
        if len(self.played_cards) == 2:  # Se ambas as cartas foram jogadas
            # Ordena as cartas jogadas pela hierarquia de Truco Paulista
            card1 = self.played_cards[0]
            card2 = self.played_cards[1]

            winner = self.determine_winner(card1, card2)

            # Atualiza a pontuação
            self.update_score(winner, 1)  # Cada rodada vencida soma 1 ponto para o vencedor
            self.played_cards.clear()  # Limpa as cartas jogadas após a rodada

            # Verifica se o jogo terminou
            for player in self.players:
                if self.scores[player.name] >= self.max_points:
                    print(f"\n{player.name} venceu o jogo com {self.scores[player.name]} pontos!")
                    self.end_game(player)
                    break

        else:
            print(f"Esperando o próximo jogador jogar a carta...")

    def determine_winner(self, card1, card2):
        """Determina o vencedor da rodada comparando as cartas jogadas."""
        card_values = {
            '4♠': 14, '7♠': 13, '7♥': 12, 'A♠': 11, 'A♥': 10, 'A♦': 9, 'A♣': 8,
            '3♠': 7, '3♥': 6, '3♦': 5, '3♣': 4, '2♠': 3, '2♥': 2, '2♦': 1, '2♣': 0,
            'K♠': 19, 'K♥': 18, 'K♦': 17, 'K♣': 16,
            'Q♠': 15, 'Q♥': 14, 'Q♦': 13, 'Q♣': 12,
            'J♠': 11, 'J♥': 10, 'J♦': 9, 'J♣': 8,
            '10♠': 7, '10♥': 6, '10♦': 5, '10♣': 4,
            '9♠': 3, '9♥': 2, '9♦': 1, '9♣': 0,
            '7♦': 5, '7♣': 4, '6♠': 2, '6♥': 1, '6♦': 0, '6♣': -1,
            '5♠': -2, '5♥': -3, '5♦': -4, '5♣': -5,
            '4♦': -6, '4♣': -7
        }
        
        value1 = card_values.get(card1, 0)
        value2 = card_values.get(card2, 0)

        if value1 > value2:
            return self.played_cards[0].player  
        elif value2 > value1:
            return self.played_cards[1].player  
        else:
            print("Empate! Nenhuma carta venceu.")
            return None  


