class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_dict = {}
        self.order = []

    @property
    def cache(self):
        key = self.order[0]
        return key, self.cache_dict[key]

    @cache.setter
    def cache(self, new_elem):
        key, value = new_elem

        if key in self.cache_dict:
            self.order.remove(key)
        elif len(self.cache_dict) >= self.capacity:
            oldest_key = self.order.pop(0)
            del self.cache_dict[oldest_key]
        self.order.append(key)
        self.cache_dict[key] = value

    def get(self, key):
        if key in self.cache_dict:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_dict[key]
        else:
            return None

    def print_cache(self):
        print("LRU Cache:")
        for key in self.order:
            print(f"{key} : {self.cache_dict[key]}")
cache = LRUCache(3)
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")
cache.print_cache()
print(cache.get("key2"))
cache.cache = ("key4", "value4")
cache.print_cache()
