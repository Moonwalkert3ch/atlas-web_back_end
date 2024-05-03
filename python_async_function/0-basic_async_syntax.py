#!/usr/bin/env python3
"""Defines an asynchronous routine"""

import asyncio
import random


async def wait_random(max_delay=10):
    """Returns a random delay between 0 and max_delay
    Paramater Args: max_delay(int) - is the max delay amount
    Return: random number between 0 and 10
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def main():
    """Create entry point function"""
    random_delay = await wait_random()
    print(f"Waited for {random_delay} seconds")

asyncio.run(main())
