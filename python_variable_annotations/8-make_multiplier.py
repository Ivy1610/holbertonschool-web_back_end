#!/usr/bin/env python3
"""
type-annotated function make_multiplier that takes a float multiplier as
argument and returns a function that multiplies a float by multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier - takes a float multiplier as argument

    Args:
        multiplier (float): The float to multiply by

    Returns:
        Callable[[float], float]: A function that multiplies
        a float by multiplier
    """
    def multiply(n: float) -> float:
        """
        multiply - takes a float n as argument

        Args:
            n (float): The float to multiply by multiplier

        Returns:
            float: The result of multiplying n by multiplier
        """
        return n * multiplier
    return multiply
