from abc import ABC, abstractmethod

class IRound(ABC):
    @abstractmethod
    def start_round(self):
        pass

    @abstractmethod
    def determine_winner(self):
        pass
