from abc import ABC, abstractmethod

class IPlayer(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def play_card(self, card):
        pass

    @abstractmethod
    def call_truco(self):
        pass

    @abstractmethod
    def accept_truco(self):
        pass

    @abstractmethod
    def refuse_truco(self):
        pass
