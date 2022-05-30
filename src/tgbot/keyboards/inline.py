from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings.text import BUTTONS_TEXT


def profile_keyboard(have_address: bool = False) -> InlineKeyboardMarkup:
    """ Return profile keyboard """
    keyboard = InlineKeyboardMarkup()
    if have_address:
        keyboard.add(
            InlineKeyboardButton(BUTTONS_TEXT["CHANGE_STATUS"], callback_data="change_status"),
        )
    return keyboard


def get_info_keyboard(have_an_address: bool) -> InlineKeyboardMarkup:
    """ Return `get info` keyboard """
    keyboard = InlineKeyboardMarkup()
    if not have_an_address:
        keyboard.add(
            InlineKeyboardButton(BUTTONS_TEXT["GET_INFO_OK"], callback_data="get_address"),
            InlineKeyboardButton(BUTTONS_TEXT["GET_INFO_NO_THANKS"], callback_data="menu"),
        )
    return keyboard


def get_status_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(BUTTONS_TEXT["STATUS_USED"], callback_data="status#used"))
    keyboard.add(
        InlineKeyboardButton(BUTTONS_TEXT['STATUS_HOLD'], callback_data="status#hold"))
    return keyboard


def time_choice_keyboard():
    keyboard = InlineKeyboardMarkup()
    for hour in range(0, 24, 2):
        keyboard.add(
            InlineKeyboardButton(f"{hour:02}:00", callback_data=f"{hour:02}:00"),
            InlineKeyboardButton(f"{hour + 1:02}:00", callback_data=f"{hour + 1:02}:00"),
        )
    return keyboard
