from abc import ABC, abstractmethod

class IObserver(ABC):
    @abstractmethod
    def update(self, message: str):
        """Método chamado quando o sujeito notifica o observador."""
        pass
