#!/usr/bin/env python3
"""
Annotate the below function’s parameters and return values
with the appropriate types
"""

from typing import List, Tuple, Sequence


def element_length(lst):
    """
    Return a list of tuples with the string and its length

    parameters:
        lst (Sequence[str]): List of strings

    Returns:
        List[Tuple[str, int]]: List of tuples with the string
        and its length
    """
    return [(i, len(i)) for i in lst]
