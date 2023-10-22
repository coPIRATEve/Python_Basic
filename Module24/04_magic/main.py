class Element:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Element):
            if (self.name, other.name) in [('Вода', 'Воздух'), ('Воздух', 'Вода')]:
                return Storm()
            elif (self.name, other.name) in [('Вода', 'Огонь'), ('Огонь', 'Вода')]:
                return Steam()
            elif (self.name, other.name) in [('Вода', 'Земля'), ('Земля', 'Вода')]:
                return Mud()
            elif (self.name, other.name) in [('Воздух', 'Огонь'), ('Огонь', 'Воздух')]:
                return Lightning()
            elif (self.name, other.name) in [('Воздух', 'Земля'), ('Земля', 'Воздух')]:
                return Dust()
            elif (self.name, other.name) in [('Огонь', 'Земля'), ('Земля', 'Огонь')]:
                return Lava()
        return None

    def __str__(self):
        return self.name


class Storm(Element):
    def __init__(self):
        super().__init__('Шторм')


class Steam(Element):
    def __init__(self):
        super().__init__('Пар')


class Mud(Element):
    def __init__(self):
        super().__init__('Грязь')


class Lightning(Element):
    def __init__(self):
        super().__init__('Молния')


class Dust(Element):
    def __init__(self):
        super().__init__('Пыль')


class Lava(Element):
    def __init__(self):
        super().__init__('Лава')
class YourElement(Element):
    def __init__(self):
        super().__init('Ваш элемент')
