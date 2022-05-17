from typing import NamedTuple
import aiohttp
from aiogram.types.user import User

from settings.settings import BASE_API


class UserTuple(NamedTuple):
    telegram_id: int
    username: str
    using_now: bool
    current_address: bool


async def sign_up_user(user: User):
    data = {
        "telegram_id": user.id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
    }
    async with aiohttp.ClientSession() as session:
        await session.post(f"{BASE_API}users/", data=data)


async def get_user(user: User):
    async with aiohttp.ClientSession() as session:
        response = await session.get(f'{BASE_API}users/{user.id}/')
    return await response.json()


async def use_address(user: User, current_address: int):
    async with aiohttp.ClientSession() as session:
        await session.patch(
            f'{BASE_API}users/{user.id}/', data={"current_address": current_address})


def serialize_user(data: dict):
    return UserTuple(
        telegram_id=data['telegram_id'],
        username=data['username'],
        using_now=data['using_now'],
        current_address=data['current_address'],
    )
