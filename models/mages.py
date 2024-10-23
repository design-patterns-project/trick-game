class Mage:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def is_alive(self):
        return self.health > 0

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"{self.name} sofreu {amount} de dano e agora tem {self.health} de vida.")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} se curou em {amount} pontos e agora tem {self.health} de vida.")


class FireMage(Mage):
    def __init__(self, name):
        super().__init__(name)
        self.element = "Fogo"

    def attack(self, target):
        damage = 25
        print(f"{self.name} lança uma bola de fogo em {target.name} causando {damage} de dano.")
        target.take_damage(damage)


class IceMage(Mage):
    def __init__(self, name):
        super().__init__(name)
        self.element = "Gelo"

    def attack(self, target):
        damage = 20
        print(f"{self.name} lança uma rajada de gelo em {target.name} causando {damage} de dano.")
        target.take_damage(damage)


class HealerMage(Mage):
    def __init__(self, name):
        super().__init__(name)
        self.element = "Cura"

    def heal_ally(self, ally):
        healing_amount = 30
        print(f"{self.name} cura {ally.name} em {healing_amount} pontos de vida.")
        ally.heal(healing_amount)
