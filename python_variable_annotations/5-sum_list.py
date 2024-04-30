#!/usr/bin/env python3
"""Defines a function that takes a list of floats
as argument and returns their sum as a float"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns sum of list of floats
    Param arg1: input-list- list of floats
    Return: Sum of input_list
    """

    return sum(input_list)
