
from characters.interfaces.i_statistics import IStatistics


class Statistics(IStatistics):
    def __init__(self):
        self.total_wins = 0
        self.total_losses = 0

    def update_statistics(self, win: bool):
        if win:
            self.total_wins += 1
        else:
            self.total_losses += 1
