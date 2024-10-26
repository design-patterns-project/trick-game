from characters.models.card import Card
from designs_patterns.factory.interfaces.i_factory import IFactory


class CardFactory(IFactory):
    def create(self, value: str, suit: str) -> Card:
        return Card(value, suit)
