import re

from aiogram import Bot

from settings.settings import GROUP_ID


def is_valid_product_url(url: str) -> bool:
    pattern = r"http(s)?\:\/\/\w+(\.\w+)\/?(\S+)"
    return bool(re.search(pattern, url))


async def get_user_group_status(bot: Bot, user_id: int):
    response = await bot.get_chat_member(chat_id=GROUP_ID, user_id=user_id)
    return response["status"]
