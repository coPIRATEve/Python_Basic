class MyDict:
    def __init__(self):
        self.data = {}
    def __getitem__(self, key):
        return self.data.get(key, 0)

    def __setitem__(self, key, value):
        self.data[key] = value

    def get(self, key, default=None):
        return self.data.get(key, 0 if default is None else default)

    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def items(self):
        return self.data.items()

    def __str__(self):
        return str(self.data)

my_dict = MyDict()
my_dict[''] = ""
my_dict[''] = ""

print(my_dict.get(''))
print(my_dict.get(''))
print(my_dict.get('', 100))
print(my_dict.keys())
