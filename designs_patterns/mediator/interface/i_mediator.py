from abc import ABC, abstractmethod

class IMediator(ABC):
    @abstractmethod
    def notify(self, sender, event: str):
        pass
