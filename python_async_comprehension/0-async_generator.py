#!/usr/bin/env python3
"""
An async generator that takes no arguments and
yields 10 random numbers between 0 and 10.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    An async generator: that takes no arguments and
    yields 10 random numbers between 0 and 10.

    Returns:
        AsyncGenerator[float, None]: An async generator that takes
        no arguments and yields 10 random
        numbers between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
