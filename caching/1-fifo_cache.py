#!/usr/bin/env python3
""" Create a class FIFOCache that inherits from
BaseCaching and is a caching system """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """will inherit from the parent class it can be
    overloaded but we will set limits to handle this
    type situation value
    __init__ - initiates the class instance
    put - method that assigns the key/value to the dictionary
    get - method that stores the cache in the dictionary space"""

    def __init__(self):
        """initializes class instance"""
        super().__init__()

    def put(self, key, item):
        """adds the key/value to cache data"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard_key = list(self.cache_data.keys())[0]
                del self.cache_data[discard_key]
                print(f"DISCARD: {discard_key}")
            self.cache_data[key] = item
        pass

    def get(self, key):
        """stores the cache data into the key value"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
