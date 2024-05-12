#!/usr/bin/env python3
"""
Write a function named index_range that takes
two integer arguments page and page_size and
returns a tuple of size two of start/end index
"""


def index_range(page, page_size):
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
