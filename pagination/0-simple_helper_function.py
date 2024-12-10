#!/usr/bin/env python3
"""
Module for 0-simple_helper_function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calulates the start and end index for the given page and page_size

    Parameters:
    page (int): The page number
    page_size (int): The number of items per page

    Returns:
    Tuple[int, int]: A tuple of the start and end index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
