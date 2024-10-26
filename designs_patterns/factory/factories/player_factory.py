from characters.models.player import Player
from designs_patterns.factory.interfaces.i_factory import IFactory


class PlayerFactory(IFactory):
    def create(self, name: str) -> Player:
        return Player(name)
