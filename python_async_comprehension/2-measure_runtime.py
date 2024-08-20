#!/usr/bin/env python3
"""
 a measure_runtime coroutine that will execute async_comprehension four times
 in parallel using asyncio.gather.
 measure_runtime should measure the total runtime and return it.
 Notice that the total runtime is roughly 10 seconds, explain it to yourself.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime of async_comprehension
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time
    return total_runtime
