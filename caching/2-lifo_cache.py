#!/usr/bin/env python3
"""Create a class LIFOCache that inherits from
BaseCaching and is a caching system:"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system:
    put - method to assign the key/value to the dictionary
    get - method to store the cache in the dictionary space
    """

    def __init__(self):
        """Initializes class instance"""
        super().__init__()

    def put(self, key, item):
        """Adds the key/value to cache data"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard_key = list(self.cache_data.keys())[-1]
                del self.cache_data[discard_key]
                print(f"DISCARD: {discard_key}")
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value linked to the key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
