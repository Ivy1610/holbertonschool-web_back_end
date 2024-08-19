#!/usr/bin/env python3
"""
write an async routine called wait_n that takes in
2 int arguments
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that takes in an integer argument

    Args:
        n (int): number of iterations
        max_delay (int): max delay

    Returns:
        List[float]: list of delays
    """
    delays = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]


