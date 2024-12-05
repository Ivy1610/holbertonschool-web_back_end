#!/usr/bin/env python3
"""
6-sum_mixed_list.py

Defines a function `sum_mixed_list` that takes a list
of integers and floats and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Computes the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]):
            A list containing integers and/or floats.

    Returns:
        float: The sum of all elements in the list as a float.
    """
    return float(sum(mxd_lst))
