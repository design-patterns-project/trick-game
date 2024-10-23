from interfaces import IObserver

class ConsoleObserver(IObserver):
    def update(self, message):
        print(message)
