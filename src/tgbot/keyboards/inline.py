from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def menu_keyboard() -> InlineKeyboardMarkup:
    """
    Return a menu keyboard with this buttons:

    | get info | profile |
    |--------------------|
    |     get contacts   |
    """
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton("get info", callback_data="menu#get_info"),
        InlineKeyboardButton("profile", callback_data="menu#profile"),
    )
    keyboard.add(InlineKeyboardButton("get contacts", callback_data="menu#get_contacts"))
    return keyboard
