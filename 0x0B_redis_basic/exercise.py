#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """defines decorater that counts how many times
    cache class has been called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """"defines wrapper function"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

class Cache:
    """stores Redis client instance"""
    def __init__(self):
        """create redis client instance"""
        # store an instance of redis client as private var
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        stores input data and returns it
        Paramater args: Data(Union) - generated random uuid
        Return - random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[callable]) -> Union[str, bytes, int, float]:
        """converts data back to desired format
        Param Args: key(str) - key to convert
        fn(optional(callable)) - optional function to convert
        Return - converted data
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """parameterize value to string"""
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        """parameterize value to int"""
        value = self._redis.get(key)
        try:
            if value is None:
                return 0 # returns default value
            return int(value.decode('utf-8'))
        except ValueError:
            return TypeError(int(Callable)) # handles con
