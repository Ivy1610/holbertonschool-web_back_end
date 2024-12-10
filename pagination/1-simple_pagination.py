#!/usr/bin/env python3
"""
Module for 1-simple_pagination
"""
import csv
import math
from typing import Tuple, List


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


class Server:
    """Server class to paginate a database of popular baby names.

    Attributes:
        DATA_FILE (str): The path to the dataset file

    Methods:
        dataset(self) -> List[List]: Cached dataset
        get_page(self, page: int = 1, page_size: int = 10)
                -> List[List]: Get a page of the dataset
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset

        Returns:
            List[List]: The dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns the proper page of the dataset

        Parameters:
            page (int): The page number
            page_size (int): The number of items per page

        Returns:
            List[List]: The page of the dataset
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_index:end_index]
