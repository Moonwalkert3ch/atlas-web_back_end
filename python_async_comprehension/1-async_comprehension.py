#!/usr/bin/env python3
"""write a coroutine called async_comprehension
that takes no arguments. The coroutine will collect
10 random numbers using an async comprehensing over
async_generator, then return the 10 random numbers.
"""

import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Returns a coroutine that will collect 10 random numbers
    using an async comprehensing over async_generator, then
    return the 10 random numbers
    Return(float) - List of 10 random numbers.
    """
    return [numbers async for numbers in async_generator()]
