#!/usr/bin/env python3
"""index_range Module"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of size two containing a start index
    and an end index corresponding to the range of indexes to return
    in a list for those particular parameters."""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
