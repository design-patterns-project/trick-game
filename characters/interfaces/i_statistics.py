from abc import ABC, abstractmethod

class IStatistics(ABC):
    @abstractmethod
    def update_statistics(self):
        pass
