#!/usr/bin/env python3
"""Write a function (do not create an async function,
use the regular function syntax to do this) task_wait
_random that takes an integer max_delay and returns a
asyncio.Task."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns a asyncio.task
    Parameter Args1: max_delay(int) - max amount of delays
    Return - asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
