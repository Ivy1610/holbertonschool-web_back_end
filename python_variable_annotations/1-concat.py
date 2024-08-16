#!/usr/bin/env python3
"""
type-annotated function concat that takes a string str1 and
a string str2 as arguments and returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings

    Args:
        str1 (str): First string
        str2 (str): Second string

    Returns:
        str: Concatenated string
    """
    return str1 + str2
