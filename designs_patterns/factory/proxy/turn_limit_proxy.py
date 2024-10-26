from designs_patterns.factory.proxy.interface.i_proxy import PlayerProxyInterface
from designs_patterns.factory.proxy.player_proxy import PlayerProxy


class TurnLimitProxy(PlayerProxyInterface):
    def __init__(self, player, game):
        self.player = player
        self.game = game

    def play_card(self, card):
        if self.game.is_turn_limit_exceeded():
            print(f"O limite de jogadas foi alcançado. {self.player.name} não pode jogar.")
            return

        # Delegar a ação para o PlayerProxy padrão
        player_proxy = PlayerProxy(self.player, self.game)
        player_proxy.play_card(card)
