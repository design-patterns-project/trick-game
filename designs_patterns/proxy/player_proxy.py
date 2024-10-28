from characters.models.player import Player
from characters.models.card import Card
from characters.interfaces.i_game import GameInterface
from designs_patterns.proxy.interfaces.i_proxy import IPlayerProxy

class PlayerProxy(IPlayerProxy):
    def __init__(self, player: Player, game: GameInterface):
        self.player = player
        self.game = game

    def play_card(self, card: Card) -> None:
        if self.game.is_player_turn(self.player):
            self.player.play_card(card)
            print(f"{self.player.name} jogou a carta {card.value} de {card.suit}.")
        else:
            print(f"{self.player.name} não pode jogar agora, não é sua vez.")
