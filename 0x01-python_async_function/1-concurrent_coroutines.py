#!/usr/bin/env python3
"""
You will spawn wait_random n times with the specified max_delay.
"""
wait_random = __import__('0-basic_async_syntax').wait_random


def sorting(lst: list) -> list:
    """
    lst : list
    """
    r: list = lst[:]
    s = []
    for i in range(len(lst)):
        s.append(min(r))
        r.pop(min(r))
    return s


async def wait_n(n: int, max_delay: int) -> list:
    """
    n : int
    max_delay : int
    return : list
    """
    r = []
    for i in range(n):
        r.append(await wait_random(max_delay))
    return sorting(r)
