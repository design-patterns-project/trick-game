from designs.factory import MageFactory
from designs.singleton import GameState
from designs.memento import Memento, Caretaker
from designs.strategy import AttackStrategy, DefendStrategy, SpecialAbilityStrategy
from designs.observer import ConsoleObserver


class BattleManager:
    def __init__(self):
        self.game_state = GameState()
        self.caretaker = Caretaker()

    def start_battle(self):
        observer = ConsoleObserver()

        mage1 = MageFactory.create_mage("Fogo", "Pyro")
        mage2 = MageFactory.create_mage("Gelo", "Frost")
        mage1.add_observer(observer)
        mage2.add_observer(observer)
        
        self.game_state.add_player(mage1)
        self.game_state.add_player(mage2)

        while all(player.is_alive() for player in self.game_state.players):
            current_player = self.game_state.get_current_player()
            target = self.game_state.get_other_player()
            self.save_game_state()

            action = input(f"{current_player.name}, escolha uma ação (A para atacar, D para defender, S para habilidade especial): ").upper()

            if action == "A":
                strategy = AttackStrategy()
            elif action == "D":
                strategy = DefendStrategy()
            elif action == "S":
                strategy = SpecialAbilityStrategy()
            else:
                print("Ação inválida, escolha novamente.")
                continue

            strategy.execute(current_player, target)
            if not target.is_alive():
                print(f"{target.name} foi derrotado!")
                break

            self.game_state.next_turn()

        print("A batalha terminou!")

    def save_game_state(self):
        self.caretaker.save_state(Memento(self.game_state))

    def restore_last_state(self):
        state = self.caretaker.restore_last_state()
        if state:
            self.game_state = state
            print("Estado do jogo restaurado.")

if __name__ == "__main__":
    battle_manager = BattleManager()
    battle_manager.start_battle()
