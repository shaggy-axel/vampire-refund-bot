import requests as req

from settings.settings import BASE_API


def get():
    response = req.get(f"{BASE_API}countries/").json()
    for country in response:
        yield country["id"], country["name"]
