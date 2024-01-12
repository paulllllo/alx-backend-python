#!/usr/bin/env python3
"""ALX SE"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    create multiple async coroutines
    asyncio.as_completed can be used if you don't want to use sorted()
    """
    res = await asyncio.gather(*(task_wait_random(
                               max_delay) for _ in range(n)))
    return sorted(res)
