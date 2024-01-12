#!/usr/bin/env python3
"""ALX SE"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """Generate an iterator with random values"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
