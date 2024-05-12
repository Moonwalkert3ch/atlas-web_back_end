#!/usr/bin/env python3
"""
Write a function named index_range that takes
two integer arguments page and page_size and
returns a tuple of size two of start/end index
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """
    function should return a tuple of size two
    containing a start index and an end index
    corresponding to the range of indexes to
    return in a list for those particular
    pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Implement a method named get_page that takes two
        integer arguments page with default value 1 and
        page_size with default value 10."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        row_list = len(dataset)
        start_index, end_index = index_range(page, page_size)

        if start_index >= row_list:
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Implement a get_hyper method that takes the same
        arguments (and defaults) as get_page and returns
        a dictionary containing the following key-value
        pairs:

        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from
        previous task)
        next_page: number of the next page, None if no next
        page
        prev_page: number of the previous page, None if no
        previous page
        total_pages: the total number of pages in the dataset
        as an integer
        """
        data_content = self.get_page(page, page_size)
        row_list = len(self.dataset())
        total_pages = math.ceil(row_list / page_size)

        next_page = page + 1 if end_index < row_list else None
        prev_page =  page - 1 if page > 1 else None

        return {
            "page_size": len(data_content),
            "page": page,
            "data": data_content,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
