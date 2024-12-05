#!/usr/bin/env python3
"""
8-make_multilier.py

This module define a function `make_multiplier` that creates
a multiplier function
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a specified multiplier

    Args:
        multiplier (float): multiplier value

    Returns:
        Callable[[float], float]: function that takes a
        float and returns its product with the multipier
    """
    return lambda x: x * multiplier
