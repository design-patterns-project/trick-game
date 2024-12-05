from designs_patterns.factory.proxy.interface.i_proxy import PlayerProxyInterface


class PlayerProxy(PlayerProxyInterface):
    def __init__(self, player, game):
        self.player = player
        self.game = game

    def play_card(self, card):
        if not self.game.is_player_turn(self.player):
            print(f"Não é a vez de {self.player.name} jogar.")
            return

        if not self.player.has_card(card):
            print(f"{self.player.name} não tem a carta {card}.")
            return

        if not self.game.is_valid_play(card):
            print(f"A jogada com a carta {card} não é válida.")
            return

        if self.game.is_game_over():
            print("O jogo já terminou. Nenhum jogador pode jogar.")
            return
        
        # Chama o método real de jogar a carta
        self.player.play_card(card)
        print(f"{self.player.name} jogou a carta {card}.")
