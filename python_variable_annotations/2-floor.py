#!/usr/bin/env python3
"""
type-annotated function floor which takes a float n
as argument and returns the floor of the float.
"""

import math


def floor(n: float) -> int:
    """
    Return the floor of a float

    Args:
        n (float): The float number

    Returns:
        int: The floor of the float
    """
    return math.floor(n)
