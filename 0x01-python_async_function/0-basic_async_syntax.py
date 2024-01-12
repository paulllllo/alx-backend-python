#!/usr/bin/env python3
"""ALX SE"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """perform a simple async function"""
    time = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
