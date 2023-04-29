#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into
a new function task_wait_n.
"""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random
sorting = __import__('1-concurrent_coroutines').sorting


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    n : int
    max_delay : int
    return : list
    """
    r = []
    for i in range(n):
        r.append(await task_wait_random(max_delay))
    return sorting(r)
