#!/usr/bin/env python3
""" Create a class FIFOCache that inherits from
BaseCaching and is a caching system """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """will inherit from the parent class it can be
    overloaded but we will set limits to handle this
    type situation value
    put - assigned the key/value to the dictionary
    get - stores the cache in the dictionary space"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
               discard_key = next(iter(self.cache_data))
               del self.cache_data[discard_key]
               print(f"DISCARD: {discard_key}\n")
            self.cache_data[key] = item
