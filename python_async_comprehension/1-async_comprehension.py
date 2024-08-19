#!/usr/bin/env python3
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    An async comprehensions that takes no arguments and
    returns a list of 10 random numbers between 0 and 10.

    Returns:
        List[float]: A list of 10 random numbers between 0 and 10.
    """
    return [i async for i in async_generator()]
