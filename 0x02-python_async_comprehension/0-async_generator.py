#!/usr/bin/env python3
"""
Write a coroutine called async_generator that
takes no arguments.
"""
import asyncio
from random import uniform


async def async_generator() -> float:
    """
    _return_ :
    """
    for i in range(10):
        yield uniform(0, 10)
        await asyncio.sleep(1)
