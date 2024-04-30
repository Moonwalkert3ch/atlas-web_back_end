#!/usr/bin/env python3
"""Defines a function that takes a string and an
int or float as args and returns as a tuple """

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a string key and an int/float value to
    a tuple.
    Parameter
    Args1: k(str) - string key
    V(int, float) - integer or float value
    Return: tuple with arg values
    """

    return k, float(v ** 2)
