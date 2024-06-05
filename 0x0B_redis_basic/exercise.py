#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """defines decorater that counts how many times
    cache class has been called"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """"defines wrapper function"""
        key = method.__qualname__  # use methods name as key
        self._redis.incr(key)  # increments redis count
        return method(self, *args, **kwargs)  # calls original method
    return wrapper


def call_history(method: Callable) -> Callable:
    """decorator stores i/o history"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """defines wrapper for history"""
        input_key = "{}:inputs".format(method.__qualname__)
        output_key = "{}:outputs".format(method.__qualname__)
        # store i/o lists in redis
        self._redis.rpush(input_key, str(args))
        # execute original method
        format_method = method(self, *args, **kwargs)
        self._redis.rpush(output_key, format_method)
        return format_method
    return wrapper


def replay(method: Callable):
    """Display history of calls for a specific method in Cache."""
    method_name = method.__qualname__
    cache = Cache()
    inputs_key = f"{method_name}:inputs"

    # Retrieve inputs from Redis
    inputs = cache._redis.lrange(inputs_key, 0, -1)

    print(f"{method_name} was called {len(inputs)} times:")
    for input_str in inputs:
        input_args = eval(input_str.decode())  # Convert string back to tuple
        print(f"{method_name}(*{input_args})")


class Cache:
    """stores Redis client instance"""

    def __init__(self):
        """create redis client instance"""
        # store an instance of redis client as private var
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        stores input data and returns it
        Paramater args: Data(Union) - generated random uuid
        Return - random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[callable]
            = None) -> Union[str, bytes, int, float]:
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
        return value.decode('utf-8') if value else ''

    def get_int(self, key: str) -> int:
        """parameterize value to int"""
        value = self._redis.get(key)
        if value is None:
            return 0  # returns default value
        try:
            return int(value.decode('utf-8'))
        except ValueError:
            return 0
