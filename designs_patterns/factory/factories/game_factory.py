from typing import List

from characters.models.game import Game
from characters.models.player import Player
from designs_patterns.factory.interfaces.i_factory import IFactory
from designs_patterns.mediator.game_mediator import GameMediator  

class GameFactory(IFactory):
    def create(self, players: List[Player], mediator: GameMediator) -> Game:
        return Game(players, mediator)  
