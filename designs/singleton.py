from interfaces import ISingleton

class GameState(ISingleton):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameState, cls).__new__(cls)
            cls._instance.reset()
        return cls._instance

    def reset(self):
        self.players = []
        self.turn = 0

    def add_player(self, player):
        self.players.append(player)

    def next_turn(self):
        self.turn = (self.turn + 1) % len(self.players)

    def get_current_player(self):
        return self.players[self.turn]

    def get_other_player(self):
        return self.players[(self.turn + 1) % len(self.players)]
