from datetime import datetime
from typing import NamedTuple, Optional, Union

import aiohttp

from settings.settings import BASE_API


class AddressTuple(NamedTuple):
    id: int
    name: str
    line_1: str
    line_2: str
    city: str
    state: str
    zip_code: int
    phone: str
    status: str
    used_by: Optional[int]
    used_at: Optional[Union[str, datetime]]


async def get_addresses(status: str = "all"):
    async with aiohttp.ClientSession() as session:
        if status == 'used':
            response = await session.get(f"{BASE_API}addresses/?status=used")
        elif status == 'notused':
            response = await session.get(f"{BASE_API}addresses/?status=notused")
        elif status == 'hold':
            response = await session.get(f"{BASE_API}addresses/?status=hold")
        else:
            response = await session.get(f"{BASE_API}addresses/")
    return await response.json()


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
            used_at=data["used_at"]
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
            used_at=address["used_at"]
        ) for address in data
    ]


def update_address(status: str = "used"):
    used_at = None
    if status == "used":
        used_at = f"{datetime.now():%Y-%m-%d %H:%M}"
    return used_at
