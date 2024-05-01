#!/usr/bin/env python3
"""Defines a function that iterates through
the input list"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:   
    """Returns the values in the list
    Parameters Args: lst(Iterable[Sequence]) - the iterable object.
    Returns: List[Tuple[Sequence, int]] - the list of tuples"""

    return [(i, len(i)) for i in lst]
