from aiogram import Dispatcher, types
from settings.settings import MESSAGE_TEXT

from tgbot.keyboards.inline import (
    address_page, get_info_keyboard,
    get_status_keyboard, menu_keyboard, profile_keyboard)
from tgbot.services import addresses_api, telegram_user_api


async def back_to_menu(callback: types.CallbackQuery):
    callback.message.from_user.id = callback.from_user.id
    await user_start(callback.message)


async def user_start(message: types.Message):
    text = MESSAGE_TEXT["START_COMMAND"]

    if not message.get_command():
        pass
    elif "start" in message.get_command():
        text = MESSAGE_TEXT["MENU_COMMAND"]
        telegram_user_api.sign_up_user(message.from_user)

    keyboard = menu_keyboard()
    await message.bot.send_message(message.from_user.id, text, reply_markup=keyboard)
    await message.bot.delete_message(
        message.chat.id, message.message_id
    )


async def get_profile(message: types.Message):
    data = telegram_user_api.get_user(message.from_user)
    user = telegram_user_api.serialize_user(data)
    if user.current_address:
        data = addresses_api.get_address(user.current_address)
        address = addresses_api.serialize_addresses(data)
        text = MESSAGE_TEXT["PROFILE_IF_HAVE_ADDRESS"].format(
            username=user.username, address_name=address.name,
            address_line_1=address.line_1, address_line_2=address.line_2,
            address_city=address.city, address_state=address.state,
            address_zip_code=address.zip_code, address_phone=address.phone
        )
    else:
        text = MESSAGE_TEXT["PROFILE_IF_HAVE_NO_ADDRESS"].format(username=user.username)

    await message.bot.send_message(
        message.from_user.id, text,
        reply_markup=profile_keyboard(bool(user.current_address)))
    await message.bot.delete_message(
        message.from_user.id, message.message_id,
    )


async def get_info(message: types.Message):
    data = telegram_user_api.get_user(message.from_user)
    user = telegram_user_api.serialize_user(data)
    text = MESSAGE_TEXT["GET_INFO_IF_HAVE_NO_ADDRESS"].format(
        first_name=message.from_user.first_name)
    if user.current_address:
        text = MESSAGE_TEXT["GET_INFO_IF_HAVE_ADDRESS"]
    await message.bot.send_message(
        message.from_user.id, text,
        reply_markup=get_info_keyboard(bool(user.current_address)),
        parse_mode='Markdown')
    await message.bot.delete_message(
        message.chat.id, message.message_id
    )


async def get_addresses(callback: types.CallbackQuery):
    data = addresses_api.get_addresses()
    addresses = addresses_api.serialize_addresses(data)
    telegram_user_api.use_address(callback.from_user, addresses.id)
    callback.message.from_user = callback.from_user
    await get_profile(callback.message)


async def get_address(callback: types.CallbackQuery):
    address_id = callback.data.split('#')[1]
    data = addresses_api.get_address(address_id)
    address_data = addresses_api.serialize_addresses(data)
    text = (
        "⬇️ Shipping address ⬇️\n"
        f"**Name**: `{address_data.name}`\n"
        f"__Line 1__: `{address_data.line_1}`\n"
        f"__Line 2__: `{address_data.line_2}`\n"
        f"**City**: `{address_data.city}`\n"
        f"**State**: `{address_data.state}`\n"
        f"**ZIP**: `{address_data.zip_code}`\n"
        f"**Phone number**: `{address_data.phone}`\n\n"
    )
    if address_data.using_now:
        text += "This address now using"

    await callback.bot.send_message(
        callback.from_user.id, text,
        reply_markup=address_page(address_data.id, address_data.using_now),
        parse_mode='Markdown'
    )
    await callback.bot.delete_message(
        callback.message.chat.id, callback.message.message_id
    )


async def use_address(callback: types.CallbackQuery):
    _, address_id = callback.data.split('#')
    await telegram_user_api.use_address(callback.from_user, address_id)
    await back_to_menu(callback)


async def change_status_choice(callback: types.CallbackQuery):
    keyboard = get_status_keyboard()
    text = MESSAGE_TEXT["CHOICES_STATUS_FOR_ADDRESS"]
    await callback.bot.send_message(callback.from_user.id, text, reply_markup=keyboard)
    await callback.bot.delete_message(callback.from_user.id, callback.message.message_id)


async def change_status_send(callback: types.CallbackQuery):
    status = callback.data.split('#')[1]
    data = telegram_user_api.get_user(callback.from_user)
    user = telegram_user_api.serialize_user(data)

    addresses_api.change_status(address_id=user.current_address, status=status)
    await back_to_menu(callback)


async def get_contacts(message: types.Message):
    text = MESSAGE_TEXT["GET_CONTACTS_COMMAND"]
    await message.bot.send_message(
        message.from_user.id, text)
    await message.bot.delete_message(
        message.from_user.id, message.message_id
    )


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start", "menu"], state="*")
    dp.register_callback_query_handler(
        back_to_menu, lambda callback: callback.data == 'menu')
    dp.register_message_handler(
        get_profile, lambda message: 'Profile' in message.text, state="*")
    dp.register_message_handler(
        get_info, lambda message: 'Get Info' in message.text, state="*")
    dp.register_callback_query_handler(
        get_addresses, lambda callback: callback.data.split('#')[0] == 'get_address')
    dp.register_callback_query_handler(
        get_address, lambda callback: callback.data.split('#')[0] == 'address_page')
    dp.register_callback_query_handler(
        use_address, lambda callback: callback.data.split('#')[0] == 'use_address')
    dp.register_callback_query_handler(
        change_status_choice, lambda callback: 'change_status' == callback.data)
    dp.register_callback_query_handler(
        change_status_send, lambda callback: 'status' == callback.data.split('#')[0])
    dp.register_message_handler(
        get_contacts, lambda message: 'Contacts' in message.text)
