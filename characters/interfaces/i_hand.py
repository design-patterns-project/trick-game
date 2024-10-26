from abc import ABC, abstractmethod

class IHand(ABC):
    @abstractmethod
    def calculate_points(self):
        pass
