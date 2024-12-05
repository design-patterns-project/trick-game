class GameManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameManager, cls).__new__(cls)
            cls._instance.setup_complete = False
        return cls._instance

    def setup_game(self):
        if not self.setup_complete:
            print("Configuração do jogo realizada.")
            self.setup_complete = True
