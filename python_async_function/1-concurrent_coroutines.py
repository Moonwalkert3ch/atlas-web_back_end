#!/usr/bin/env python3
"""Define an async routine that returns the list of all
the random delay float values"""
import asyncio
from typing import List
import random
import importlib.util


spec = importlib.util.spec_from_file_location("basic_async_syntax", "/home/moonwalker/atlas-web_back_end/python_async_function/0-basic_async_syntax.py")
basic_async_syntax = importlib.util.module_from_spec(spec)
spec.loader.exec_module(basic_async_syntax)
wait_random = basic_async_syntax.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns list of all random delays
    Parameter Args1: n(int) - amount of times wait_random called
    Args2: max_delay(int) - max amount of random delay count
    Return - list of delays
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
