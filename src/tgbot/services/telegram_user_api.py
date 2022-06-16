from typing import Union
import requests as req
from aiogram.types.user import User

from settings.settings import BASE_API
from tgbot.models import UserTuple
from tgbot.services.serializers import serialize_user


def sign_up_user(user: User):
    data = {
        "telegram_id": user.id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
    }
    req.post(f"{BASE_API}users/", data=data)


def get_user(user_id: Union[int, str]) -> dict:
    response = req.get(f'{BASE_API}users/{user_id}/')
    return response.json()


def is_admin(user: User) -> bool:
    data = get_user(user.id)
    return data['is_admin']


def use_address(user: User, current_address: int):
    req.patch(f'{BASE_API}users/{user.id}/', data={"current_address": current_address})


def get_all_admin_users() -> list[UserTuple]:
    response = req.get(f"{BASE_API}users/?is_admin=true")
    return serialize_user(response.json())
