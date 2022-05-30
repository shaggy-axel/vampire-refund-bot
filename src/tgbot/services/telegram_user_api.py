from typing import NamedTuple

import requests as req
from aiogram.types.user import User

from settings.settings import BASE_API


class UserTuple(NamedTuple):
    telegram_id: int
    username: str
    using_now: bool
    current_address: bool


def sign_up_user(user: User):
    data = {
        "telegram_id": user.id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
    }
    req.post(f"{BASE_API}users/", data=data)


def get_user(user: User):
    response = req.get(f'{BASE_API}users/{user.id}/')
    return response.json()


def use_address(user: User, current_address: int):
    req.patch(f'{BASE_API}users/{user.id}/', data={"current_address": current_address})


def serialize_user(data: dict) -> UserTuple:
    try:
        return UserTuple(
            telegram_id=data['telegram_id'],
            username=data['username'],
            using_now=data['using_now'],
            current_address=data['current_address'],
        )
    except KeyError:
        raise KeyError(str(data))
