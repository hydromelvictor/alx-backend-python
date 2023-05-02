#!/usr/bin/env python3
"""
measure_runtime should measure the total
runtime and return it.
"""
import asyncio
import time
comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    _return_:
    """
    s = time.perf_counter()
    await asyncio.gather(comp(), comp(), comp(), comp())
    l = time.perf_counter() - s
    return l
