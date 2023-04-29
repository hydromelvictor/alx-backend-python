#!/usr/bin/env python3
"""
You will spawn wait_random n times with the specified max_delay.
"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def little(lst: List[float]) -> float:
    """
    lst : List[float]
    """
    min = lst[0]
    for i in lst:
        if min > i:
            min = i
    return min


def sorting(lst: List[float]) -> List[float]:
    """
    lst : list
    """
    r: list = lst[:]
    s = []
    for i in range(len(lst)):
        s.append(little(r))
        r.remove(little(r))
    return s


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    n : int
    max_delay : int
    return : list
    """
    r = []
    for i in range(n):
        r.append(await wait_random(max_delay))
    return sorting(r)
