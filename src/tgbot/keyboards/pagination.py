from aiogram import types
from settings.text import BUTTONS_TEXT

from tgbot.keyboards.paginator import InlineKeyboardPaginator, fill_paginator
from tgbot.services import addresses_api
from tgbot.services.utils import count_pages


def get_orders_keyboard(current_page: int = 1):
    addresses = addresses_api.serialize_addresses(addresses_api.get_used_addresses())
    paginator = InlineKeyboardPaginator(
        page_count=count_pages(addresses), current_page=current_page,
        data_pattern=('orders#{page}'))
    return fill_paginator(
        data=addresses, data_fields=("country", "product_id"),
        callback_data_prefix="order", callback_data_field="id",
        previous_keyboard_callback="menu", paginator=paginator)


def get_back_to_orders_keyboard(
    address_id: str, current_page: int = 1
) -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup()
    keyboard.insert(types.InlineKeyboardButton(
        BUTTONS_TEXT["DELIVERED"], callback_data=f"delivered#{address_id}"))
    keyboard.add(types.InlineKeyboardButton(
        BUTTONS_TEXT["BACK_TO_ORDERS"], callback_data=f"orders#{current_page}"))
    keyboard.insert(types.InlineKeyboardButton(
        BUTTONS_TEXT["BACK_TO_MENU"], callback_data="menu"))
    return keyboard
