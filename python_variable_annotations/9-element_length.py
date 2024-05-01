#!/usr/bin/env python3
"""Defines a function that iterates through
the input list"""

from typing import Iterable, List, Tuple


def element_length(lst: Iterable) -> List[Tuple]:   
    """Returns the values in the list
    Parameters Args: lst(Iterable) - the iterable object.
    Returns: List[Tuple] - the list of tuples"""

    return [(i, len(i)) for i in lst]
