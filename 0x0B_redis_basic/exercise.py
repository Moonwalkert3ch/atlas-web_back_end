#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union


class Cache:
    """stores Redis client instance"""
    def __init__(self):
        """create redis client instance"""
        # store an instance of redis client as private var
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        stores input data and returns it
        Paramater args: Data(Union) - generated random uuid
        Return - random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
