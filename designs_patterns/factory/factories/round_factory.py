from typing import List

from characters.models.player import Player
from characters.models.round import Round
from designs_patterns.factory.interfaces.i_factory import IFactory
from designs_patterns.mediator.game_mediator import GameMediator

class RoundFactory(IFactory):
    def create(self, players: List[Player], mediator: GameMediator) -> Round:
        return Round(players, mediator)
