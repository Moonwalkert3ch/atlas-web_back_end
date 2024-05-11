#!/usr?bin/env python3
"""Create a class BasicCache that inherits from
BaseCoaching and is a caching system"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Create a class BasicCache that inherits from
    BaseCaching and is a caching system
    Attributes: put - method that adds key/value to item
    get - method to store the cache in key/value
    """

    def put(self, key, item):
        """Adds key/value pair to item"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves the value stored in key cache"""
        if key is not None:
            return self.cache_data.get(key)
        return None
