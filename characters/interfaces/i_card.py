from abc import ABC, abstractmethod

class ICard(ABC):
    @abstractmethod
    def compare(self, other):
        pass
