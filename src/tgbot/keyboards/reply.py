from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from settings.text import BUTTONS_TEXT


def menu_keyboard(is_admin: bool = False) -> ReplyKeyboardMarkup:
    """ Return a menu keyboard with this buttons """
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    if is_admin:
        keyboard.add(
            KeyboardButton(BUTTONS_TEXT['ORDERS']),
            KeyboardButton(BUTTONS_TEXT['CREATE_ADDRESS']),
        )
    else:
        keyboard.add(KeyboardButton(BUTTONS_TEXT["CONTACTS"]))

    keyboard.add(
        KeyboardButton(BUTTONS_TEXT['GET_INFO']),
        KeyboardButton(BUTTONS_TEXT['PROFILE']),
    )

    return keyboard
