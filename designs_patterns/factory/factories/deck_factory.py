from characters.models.deck import Deck
from designs_patterns.factory.interfaces.i_factory import IFactory


class DeckFactory(IFactory):
    def create(self) -> Deck:
        return Deck()
