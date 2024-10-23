from abc import ABC, abstractmethod

# Interface para o padrão Strategy
class IStrategy(ABC):
    @abstractmethod
    def execute(self, player, target):
        pass

# Interface para o padrão Observer
class IObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass

# Interface para o padrão Factory
class IMageFactory(ABC):
    @abstractmethod
    def create_mage(self, mage_type, name):
        pass

# Interface para o padrão Memento
class IMemento(ABC):
    @abstractmethod
    def get_saved_state(self):
        pass

# Interface para o padrão Singleton
class ISingleton(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def add_player(self, player):
        pass

    @abstractmethod
    def next_turn(self):
        pass
