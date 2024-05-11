#!/usr?bin/env python3
"""Create a class BasicCache that inherits from
BaseCoaching and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Create a class BasicCache that inherits from
    BaseCaching and is a caching system"""

    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        if key is not None:
            return self.cache_data.get(key)
        return None
