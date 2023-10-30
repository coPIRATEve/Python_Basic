class Element:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return None

    def __str__(self):
        return self.name

class Water(Element):
    def __init__(self):
        super().__init__('Вода')
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mud()
        return None

class Air(Element):
    def __init__(self):
        super().__init__('Воздух')

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        return None

class Fire(Element):
    def __init__(self):
        super().__init__('Огонь')

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        return None

class Earth(Element):
    def __init__(self):
        super().__init__('Земля')

class Storm(Element):
    def __init__(self):
        super().__init('Шторм')

class Steam(Element):
    def __init__(self):
        super().__init('Пар')

class Mud(Element):
    def __init__(self):
        super().__init('Грязь')

class Lightning(Element):
    def __init__(self):
        super().__init('Молния')

class Dust(Element):
    def __init__(self):
        super().__init('Пыль')

class Lava(Element):
    def __init__(self):
        super().__init('Лава')


water = Water()
air = Air()
fire = Fire()
earth = Earth()

result = water + air
if result:
    print(f"Результат: {result}")
else:
    print("Комбинация не определена.")
