from datetime import datetime
from typing import NamedTuple, Optional, Union

import requests as req

from settings.settings import BASE_API


class AddressTuple(NamedTuple):
    id: int
    name: str
    line_1: str
    line_2: str
    city: str
    state: str
    zip_code: str
    phone: str
    status: str
    used_by: Optional[int]
    used_at: Optional[Union[str, datetime]]
    using_now: bool
    country: str
    user_in_group: str


def get_address_info(address_id: Union[int, str]) -> dict:
    response = req.get(f"{BASE_API}addresses-set/{address_id}/")
    return response.json()


def get_used_addresses() -> dict:
    response = req.get(f"{BASE_API}addresses/used/")
    return response.json()


def get_new_address(country: str):
    response = req.get(f"{BASE_API}addresses/first/?country={country}")
    return response.json()


def change_status(address_id: int, status: str = "used", user_in_group: str = "left"):
    return req.patch(
        f'{BASE_API}addresses-set/{address_id}/',
        data={"status": status, "user_in_group": user_in_group}
    ).json()


def serialize_addresses(data: Union[list[dict], dict]):
    if isinstance(data, dict):
        return AddressTuple(
            id=data["id"],
            name=data["name"],
            line_1=data["line_1"],
            line_2=data["line_2"],
            city=data["city"],
            state=data["state"],
            zip_code=data["zip_code"],
            phone=data["phone"],
            status=data["status"],
            used_by=data["used_by"],
            used_at=data["used_at"],
            using_now=data['using_now'],
            country=data['country'],
            user_in_group=data['user_in_group'],
        )
    return [
        AddressTuple(
            id=address["id"],
            name=address["name"],
            line_1=address["line_1"],
            line_2=address["line_2"],
            city=address["city"],
            state=address["state"],
            zip_code=address["zip_code"],
            phone=address["phone"],
            status=address["status"],
            used_by=address["used_by"],
            used_at=address["used_at"],
            using_now=address['using_now'],
            country=address['country'],
            user_in_group=address['user_in_group'],
        ) for address in data
    ]
