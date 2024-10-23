from interfaces import IStrategy

class AttackStrategy(IStrategy):
    def execute(self, player, target):
        player.attack_target(target)

class DefendStrategy(IStrategy):
    def execute(self, player, target):
        player.defend()

class SpecialAbilityStrategy(IStrategy):
    def execute(self, player, target):
        player.special_ability(target)
