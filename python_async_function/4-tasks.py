#!/usr/bin/env python3
"""Take the code from wait_n and alter it into a new function task_wait_n. The code is nearly identical to wait_n except task_wait_random is being called."""

import asyncio
from typing import List
import random

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns list of all random delays
    Parameter Args1: n(int) - amount of times task_wait_random called
    Args2: max_delay(int) - max amount of random delay count
    Return - list of delays
    """
    delays = []
    tasks = [asyncio.create_task(task_wait_random(max_delay)) for _ in range(n)]

    # Execute tasks concurrently and collect the results
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
