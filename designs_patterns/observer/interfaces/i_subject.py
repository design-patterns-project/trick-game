from abc import ABC, abstractmethod

from designs_patterns.observer.interfaces.i_observer import IObserver

class ISubject(ABC):
    @abstractmethod
    def attach(self, observer: IObserver):
        """Adiciona um observador à lista de observadores."""
        pass

    @abstractmethod
    def detach(self, observer: IObserver):
        """Remove um observador da lista de observadores."""
        pass

    @abstractmethod
    def notify(self, message: str):
        """Notifica todos os observadores de uma mudança."""
        pass
