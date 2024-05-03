#!/usr/bin/env python3
"""Define an async routine that returns the list of all
the random delay float values"""

import asyncio
from typing import List
import random
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns list of all random delays
    Parameter Args1: n(int) - amount of times wait_random called
    Args2: max_delay(int) - max amount of random delay count
    Return - list of delays
    """
    delays = []
    async with asyncio.TaskGroup as tg:
        for lists in range(n):
            tg.create_task(wait_random(max_delay))
        async for task in tg:
            delays.append(task.result())
    return delays
