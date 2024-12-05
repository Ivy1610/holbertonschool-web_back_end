#!/usr/bin/env python3
"""
9-element_length.py

This module defines a function `element_length` that
computes the length of elements in an iterable.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples with elements of the iterable
    and their lengths.

    Args:
        lst (Iterable[Sequence]): An iterable containing
        sequences (e.g., strings, lists).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples,
        each containing a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
