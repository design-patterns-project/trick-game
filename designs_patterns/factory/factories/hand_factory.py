
from characters.models.hand import Hand
from designs_patterns.factory.interfaces.i_factory import IFactory


class HandFactory(IFactory):
    def create(self) -> Hand:
        return Hand()
