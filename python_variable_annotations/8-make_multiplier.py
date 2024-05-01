#!/usr/bin/env python3
"""Defines a function that takes a float as an 
argument and returns it multiplied by a float"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a multiplier function.
    
    Parameter Arg1: multiplier(float) - multiplier value.
    Returns: Callable[[float], float] - float multiplied"""

    return lambda x: x * multiplier
