import requests as req

from settings.settings import BASE_API


def bind_product(data: dict):
    """ send request to create product and bind with address """
    req.post(f"{BASE_API}products/", data=data)
