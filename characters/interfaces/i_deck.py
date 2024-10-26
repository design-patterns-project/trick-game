from abc import ABC, abstractmethod

class IDeck(ABC):
    @abstractmethod
    def shuffle(self):
        pass

    @abstractmethod
    def deal_cards(self):
        pass
