import random

class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, opponent):
        damage = 20
        print(f"{self.name} атакует {opponent.name}! {opponent.name} теряет 20 здоровья.")
        opponent.health -= damage

class Battle:
    def __init__(self, warrior1, warrior2):
        self.warrior1 = warrior1
        self.warrior2 = warrior2

    def start_battle(self):
        while self.warrior1.health > 0 and self.warrior2.health > 0:
            attacker = random.choice([self.warrior1, self.warrior2])
            opponent = self.warrior1 if attacker == self.warrior2 else self.warrior2
            attacker.attack(opponent)
            print(f"{opponent.name} имеет {opponent.health} здоровья.")

        if self.warrior1.health <= 0:
            print(f"{self.warrior1.name} одержал победу!")
        else:
            print(f"{self.warrior2.name} одержал победу!")

warrior1 = Warrior("Воин 1")
warrior2 = Warrior("Воин 2")
battle = Battle(warrior1, warrior2)
battle.start_battle()

