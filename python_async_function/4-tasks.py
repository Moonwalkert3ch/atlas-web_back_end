#!/usr/bin/env python3
"""Take the code from wait_n and alter it into a new
function task_wait_n. The code is nearly identical
to wait_n except task_wait_random is being called."""

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
    spawn_task = []

    # Create tasks and add callback to collect results
    for _ in range(n):
        delayed_task = task_wait_random(max_delay)
        delayed_task.add_done_callback(lambda x: delays.append(x.result()))
        spawn_task.append(delayed_task)

    # Execute tasks concurrently
    await asyncio.gather(*spawn_task)

    return delays
