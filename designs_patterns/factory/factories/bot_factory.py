# bot_factory.py
from characters.models.bot import SimpleBot
from designs_patterns.factory.interfaces.i_factory import IFactory


class BotFactory(IFactory):
    def create(self, name: str) -> SimpleBot:
        return SimpleBot(name)
