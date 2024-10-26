from designs_patterns.factory.proxy.interface.i_proxy import PlayerProxyInterface
from designs_patterns.factory.proxy.player_proxy import PlayerProxy


class ActiveRoundProxy(PlayerProxyInterface):
    def __init__(self, player, game):
        self.player = player
        self.game = game

    def play_card(self, card):
        if not self.game.is_round_active():
            print(f"A rodada não está ativa. {self.player.name} não pode jogar.")
            return
        
        # Delegar a ação para o PlayerProxy padrão
        player_proxy = PlayerProxy(self.player, self.game)
        player_proxy.play_card(card)
