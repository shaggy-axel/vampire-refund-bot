import re

from aiogram import Bot, types

from settings.settings import GROUP_ID
from settings.text import NOTIFY_TEXT_TO_ADMINS_ABOUT_USED_ADDRESS
from tgbot.services import telegram_user_api


def is_valid_product_url(url: str) -> bool:
    pattern = r"http(s)?\:\/\/\w+(\.\w+)\/?(\S+)"
    return bool(re.search(pattern, url))


async def get_user_group_status(bot: Bot, user_id: int):
    response = await bot.get_chat_member(chat_id=GROUP_ID, user_id=user_id)
    return response["status"]


async def send_message_to_all_of_admin_users(
    callback: types.CallbackQuery, product_data: dict,
    user_data: dict, address_data: dict,
):
    """ Send message about used address, user and his product, to all of admins """

    user_data = {f"user__{key}": value for key, value in user_data.items()}
    address_data = {f"address__{key}": value for key, value in address_data.items()}
    product_data = {f"product__{key}": value for key, value in product_data.items()}
    all_data = {**user_data, **address_data, **product_data}

    for user in telegram_user_api.get_all_admin_users():
        await callback.bot.send_message(
            user.telegram_id,
            NOTIFY_TEXT_TO_ADMINS_ABOUT_USED_ADDRESS.format(**all_data).replace('_', '\_'),
            parse_mode="Markdown"
        )
