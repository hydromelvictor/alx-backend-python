#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into
a new function task_wait_n.
"""
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """
    n : int
    max_delay : int
    return : list
    """
    r = []
    for i in range(n):
        r.append(await task_wait_random(max_delay))
    return sorted(r)
