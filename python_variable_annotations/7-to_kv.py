#!/usr/bin/env python3
"""
7-to_kv.py

This module defines a function `to_kv` that converts
a string and a number to a tuple.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple with a string and the square of a number as a float.

    Args:
        k (str): A string value.
        v (Union[int, float]): An integer or float value.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string `k`
        and the second element is the square of `v` as a float.
    """
    return (k, float(v ** 2))
