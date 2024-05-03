#!/usr/bin/env python3
"""Defines an asynchronous routine"""

import asyncio
import random


async def wait_random(max_delay: float = 10) -> float:
    """Returns a random delay between 0 and max_delay
    Paramater Args: max_delay(float) - is the max delay amount
    Return: random number between 0 and 10
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def main() -> None:
    """Creates entry point function"""
    random_delay: float = await wait_random()
    print(f"Waited for {random_delay} seconds")

asyncio.run(main())
