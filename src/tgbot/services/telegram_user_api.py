import aiohttp
from aiogram.types.user import User

from settings.settings import BASE_API


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
        response = await session.get(f'{BASE_API}users/{user.id}')
    return await response.json()
