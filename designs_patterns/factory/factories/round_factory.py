from typing import List

from characters.models.player import Player
from characters.models.round import Round
from designs_patterns.factory.interfaces.i_factory import IFactory

class RoundFactory(IFactory):
    def create(self, players: List[Player]) -> Round:
        return Round(players)
