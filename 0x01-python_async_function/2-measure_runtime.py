#!/usr/bin/env python3
"""
From the previous file, import wait_n into 2-measure_runtime.py.
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    n : int
    max_delay : int
    return : flaot
    """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - s
    return total_time / float(n)
