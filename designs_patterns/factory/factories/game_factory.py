from typing import List

from characters.models.game import Game
from characters.models.player import Player
from designs_patterns.factory.interfaces.i_factory import IFactory

class GameFactory(IFactory):
    def create(self, players: List[Player]) -> Game:
        return Game(players)
