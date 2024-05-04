#!/usr/bin/env python3
"""From the  previous file, import wait_n into
2-measure_runtime.py. Create a measure_time function
with integers n and max_delay as arguments that
measures the total execution time for wait_n
(n, max_delay), and returns total_time / n.
Your function should return a float. Use the time
module to measure an approximate elapsed time."""

from asyncio import run
from typing import Any, Callable, List
from time import time,sleep
from functools import wraps

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Returns the average execution
    Parameter Args1: n(int) - number of times called
    Args2: max_delay - max amount of delays
    Return - a float measurement
    """
    total_time = 0

    for _ in range(n):
        start_time = time()
        run(wait_n(n, max_delay))
        end_time = time()
        elapsed_time = end_time - start_time
        total_time += elapsed_time

    return total_time / n
