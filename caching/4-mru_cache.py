#!/usr/bin/env python3
"""Create a class MRUCache that inherits from BaseCaching
and is a caching system:"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRUCache caching system:
    put - method to assign the key/value to the dictionary
    get - method to store the cache in the dictionary space
    """
    def __init__(self):
        """Initializes class instance"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Adds the key/value to cache data"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.order:
                    mru_key = self.order.pop(-1)
                    del self.cache_data[mru_key]
                    print(f"DISCARD: {mru_key}")
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value linked to the key"""
        if key is not None and key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
