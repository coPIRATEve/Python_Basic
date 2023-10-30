import random

class Human:
    def __init__(self, name, house):
        self.name = name
        self.fullness = 50
        self.house = house

    def eat(self):
        if self.house.food >= 10:
            food_eaten = min(20, self.house.food)
            self.fullness += food_eaten
            self.house.food -= food_eaten
            print(f"{self.name} поел и поднял {food_eaten} xp.")
        else:
            print(f"{self.name} не поел, еда кончилась.")

    def work(self):
        money_earned = random.randint(0, 50)
        self.fullness -= 10
        self.house.money += money_earned
        print(f"{self.name} пошел в мак и заработал {money_earned} денег.")

    def play(self):
        self.fullness -= 10
        print(f"{self.name} играет в доту.")

    def go_shopping(self):
        if self.house.money >= 50:
            food_bought = random.randint(20, 50)
            self.fullness -= 10
            self.house.food += food_bought
            self.house.money -= 50
            print(f"{self.name} сходил в магазин и купил {food_bought} еды.")
        else:
            print(f"{self.name} не может сходить в магазин, так нет денег.")

    def act(self):
        dice_roll = random.randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.go_shopping()
        elif self.house.money < 50:
            self.work()
        elif dice_roll == 1:
            self.work()
        elif dice_roll == 2:
            self.eat()
        else:
            self.play()

    def is_alive(self):
        return self.fullness > 0

class House:
    def __init__(self):
        self.food = 50
        self.money = 0

def main():
    house = House()
    person1 = Human("Human_1", house)
    person2 = Human("Human_2", house)

    days = 365
    for day in range(1, days + 1):
        print(f"День {day}:")

        person1.act()
        person2.act()

        if not person1.is_alive() or not person2.is_alive():
            print("экспериментуемый умер.")
            break

    print("Эксперимент завершен.")

main()

