class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []
    def introduce(self):
        print(f"Меня зовут {(self.name)}. Мне {self.age} лет.")
    def comfort(self, child):
        child.set_calm(True)
        print(f"{self.name} успокоил ребенка {child.name}")
    def feed(self, child):
        child.set_hungry(True)
        print(f"{self.name} покормил ребенка {child.name}")

class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.calm = True
        self.hungry = True
    def set_calm(self, calm):
        self.calm = calm
    def set_hungry(self, hungry):
        self.hungry = hungry

    def state_info(self):
        calm_state = "спокойное" if self.calm else "возбужденное"
        hungry_state = "голоное" if self.hungry else "сытое"
        print(f"{self.name} - {self.age} лет, состояние: {calm_state}, голод: {hungry_state}")

