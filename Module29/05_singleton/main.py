def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class Numbers:
    def __init__(self, value):
        self.value = value

obj1 = Numbers(42)
print(obj1.value)

obj2 = Numbers(99)
print(obj2.value)

print(obj1 is obj2)

