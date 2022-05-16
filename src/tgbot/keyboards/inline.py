from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.keyboards.paginator import InlineKeyboardPaginator, fill_paginator
from tgbot.misc.useful_functions import count_pages


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


def profile_keyboard() -> InlineKeyboardMarkup:
    """
    some message text with current address

    Return profile keyboard with this buttons:

    | history | change status |
    |-------------------------|
    |       back to menu      |
    """
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton("history", callback_data="profile#history"),
        InlineKeyboardButton("change status", callback_data="profile#change_status"),
    )
    keyboard.add(InlineKeyboardButton("menu", callback_data="menu"))
    return keyboard


def get_info_keyboard(have_an_address: bool) -> InlineKeyboardMarkup:
    """
    Return `get info` keyboard with this buttons:

    | OK (go to list of addresses) | No Thanks (go to menu) |
    """
    keyboard = InlineKeyboardMarkup()
    if have_an_address:
        keyboard.add(InlineKeyboardButton("Menu", callback_data="menu"))
    else:
        keyboard.add(
            InlineKeyboardButton("OK", callback_data="addresses#all#1"),
            InlineKeyboardButton("No, Thanks", callback_data="menu"),
        )
    return keyboard


def get_list_of_addresses(data, current_page, status) -> str:
    """
    write paginator

    (default not used addresses)
    ```
    | address 1 | address 2 | address 3 |
    | address 4 | address 5 | address 6 |
    | address 7 | address 8 | address 9 |
    |-----------------------------------|
    |  << 1 | < 2 | - 3 - | 4 > | 5 >>  |
    |-----------------------------------|
    |  used addresses | hold addresses  |
    ```
    """
    paginator = InlineKeyboardPaginator(
        page_count=count_pages(data), current_page=current_page,
        data_pattern=(f'addresses#{status}#' + '{page}'))
    return fill_paginator(
        data=data, data_fields=("name", "city"),
        callback_data_prefix="address_page", callback_data_field="id",
        previous_keyboard_callback="menu", paginator=paginator, without_page_in_callback=True)


def address_page(address_id: int, using_now: bool = False) -> InlineKeyboardMarkup:
    """
    some description
    If allowed to add address for user (check in db), than add button
    `| use address |`, else write message, that he already have an address.
    and always will be buttons
    | back to list | back to menu |
    """
    keyboard = InlineKeyboardMarkup()
    # check if user have an address
    if not using_now:
        keyboard.add(InlineKeyboardButton(
            'use address', callback_data=f'use_address#{address_id}'))
    keyboard.add(
        InlineKeyboardButton("Addresses", callback_data="addresses#all#1"),
        InlineKeyboardButton("Menu", callback_data="menu"),
    )
    return keyboard
