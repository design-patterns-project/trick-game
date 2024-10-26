from designs_patterns.observer.interfaces.i_observer import IObserver

class GameObserver(IObserver):
    def update(self, message: str):
        print(f"Observador recebeu notificação: {message}")
