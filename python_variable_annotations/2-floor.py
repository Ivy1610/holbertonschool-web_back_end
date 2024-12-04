#!/usr/bin/env python3
"""
2-floor.py

This module contains a type-annotated function `floor`
that computes te floor of a float
"""


import math


def floor(n: float) -> int:
    """
    Returns the floor of a float

    Args:
        n (float): Float number

    Returns:
        int: Largest integer less than or equal to n
    """
    return math.floor(n)
