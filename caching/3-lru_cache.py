#!/usr/bin/env python3
"""Create a class LRUCache that inherits from
BaseCaching and is a caching system:"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache caching system:
    put - method to assign the key/value to the dictionary
    get - method to store the cache in the dictionary space
    """
    def __init__(self):
        """Initializes class instance"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Adds the key/value to cache data"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        self.order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Returns the value linked to the key"""
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
