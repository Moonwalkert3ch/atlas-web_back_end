#!/usr/bin/env python3

"""Defines a function that takes a list of integers
and floats and returns the sum as a float"""

from typing import Union


def sum_mixed_list(mxd_lst: List[int, float]) -> float:
    """
    Returns the sum of the list
    Param Arg1: mxd_list - list of mixed int and float 
    numbers
    Return: sum as a float
    """

    return sum(mxd_lst)
