import copy
from interfaces import IMemento

class Memento(IMemento):
    def __init__(self, state):
        self.state = copy.deepcopy(state)

    def get_saved_state(self):
        return self.state

class Caretaker:
    def __init__(self):
        self.saved_states = []

    def save_state(self, memento):
        self.saved_states.append(memento)

    def restore_last_state(self):
        if self.saved_states:
            return self.saved_states.pop().get_saved_state()
        return None
