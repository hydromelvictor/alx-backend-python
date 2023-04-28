#!/usr/bin/env python3
"""
random delay between 0 and max_delay
(included and float value) seconds and eventually returns it.
"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    max_delay : int
    return : float
    """
    i = uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
