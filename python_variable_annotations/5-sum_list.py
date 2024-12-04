#!/usr/bin/env python3
"""
5-sum_list.py

This module contains a type-annotated function `sum_list`
that computes the sum of a list of floats
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats

    Args:
        input_list (List[float]): A list of float numbers

    Returns:
        float: the sum of all the floats in the list
    """
    return sum(input_list)
