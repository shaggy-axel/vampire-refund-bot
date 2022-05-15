from typing import Iterable


def count_pages(data: Iterable, page_size: int = 10) -> int:
    if len(data) % page_size == 0:
        return len(data) // page_size
    return len(data) // page_size + 1
