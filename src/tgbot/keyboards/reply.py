from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from settings.text import BUTTONS_TEXT


def menu_keyboard() -> ReplyKeyboardMarkup:
    """
    Return a menu keyboard with this buttons:

    | get info | profile |
    |--------------------|
    |     get contacts   |
    """
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        KeyboardButton(BUTTONS_TEXT['GET_INFO']),
        KeyboardButton(BUTTONS_TEXT['PROFILE']),
    )
    keyboard.add(KeyboardButton(BUTTONS_TEXT["CONTACTS"]))
    return keyboard