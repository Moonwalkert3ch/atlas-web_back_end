#!/usr/bin/python3
"""
Test
"""
import sys

try:
    FIFOCache = __import__('1-fifo_cache').FIFOCache
    from base_caching import BaseCaching

    BaseCaching.MAX_ITEMS = 1
    FIFOCache.MAX_ITEMS = 1
    my_cache = FIFOCache()
    my_cache.MAX_ITEMS = 1

    for i in range(5):
        key = "key-{}".format(i)
        value = "value-{}".format(i)
        my_cache.put(key, value)
        my_cache.print_cache()

except:
    print(sys.exc_info()[1])