import re


def is_valid_product_url(url: str) -> bool:
    pattern = r"http(s)?\:\/\/\w+(\.\w+)\/?(\S+)"
    return bool(re.search(pattern, url))
