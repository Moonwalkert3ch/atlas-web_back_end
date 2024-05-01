#!/usr/bin/env python3
"""Defines a function that iterates through
the input list"""

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Returns the values in the list
    Parameters Args: lst (List[str]) - the list of strings
    Returns: List[Tuple[str, int]] - the list of tuples"""

    return [(i, len(i)) for i in lst]
