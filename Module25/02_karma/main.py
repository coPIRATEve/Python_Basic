import random
class KillError(Exception):
    pass

class DrunkError(Exception):
    pass

class CarCrashError(Exception):
    pass

class GluttonyError(Exception):
    pass

class DepressionError(Exception):
    pass

class LifeSimulator:
    def __init__(self):
        self.karma = 0
        self.karma_goal = 500

    def one_day(self):
        try:
            karma_points = random.randint(1, 7)
            if random.random() < 0.1:
                raise random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
            self.karma += karma_points
            return karma_points
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as e:
            with open("karma.log", "a") as log_file:
                log_file.write(f"Error: {e.__class__.__name__} - Karma: {self.karma}\n")
            return 0

    def play(self):
        while self.karma < self.karma_goal:
            karma_points = self.one_day()
            print(f"Карма: {self.karma}")
        print("Просветление достигнуто!")

# Создаем объект симулятора жизни и начинаем игру
simulator = LifeSimulator()
simulator.play()

