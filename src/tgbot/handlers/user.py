from aiogram import Dispatcher, types

from tgbot.keyboards.inline import (
    address_page, back_to_menu_button, get_info_keyboard, get_list_of_addresses, menu_keyboard, profile_keyboard)
from tgbot.services import addresses_api, telegram_user_api


async def back_to_menu(callback: types.CallbackQuery):
    callback.message.from_user.id = callback.from_user.id
    await user_start(callback.message)


async def user_start(message: types.Message):
    text = "Please select an action"

    if not message.get_command():
        pass
    elif "start" in message.get_command():
        text = "Welcome!\n" + text
        await telegram_user_api.sign_up_user(message.from_user)

    keyboard = menu_keyboard()
    await message.bot.send_message(message.from_user.id, text, reply_markup=keyboard)
    await message.bot.delete_message(
        message.chat.id, message.message_id
    )


async def get_profile(callback: types.CallbackQuery):
    data = await telegram_user_api.get_user(callback.from_user)
    user = telegram_user_api.serialize_user(data)
    text = f"{user.telegram_id} | {user.username}\n"
    if user.current_address:
        data = await addresses_api.get_address(user.current_address)
        address = addresses_api.serialize_addresses(data)
        text += (
            f"{address.name}, {address.phone}, {address.city}"
        )
    else:
        text += f"No current address"

    await callback.bot.send_message(
        callback.from_user.id, text=text, reply_markup=profile_keyboard())
    await callback.bot.delete_message(
        callback.from_user.id, callback.message.message_id,
    )


async def get_info(callback: types.CallbackQuery):
    data = await telegram_user_api.get_user(callback.from_user)
    user = telegram_user_api.serialize_user(data)
    text = (
        f"{callback.from_user.first_name}, please check our price. It's okay?\n\n"
        "Receive the parcel – $80\n"
        "CDEK ~ $25\n\n"
        "RU Bank of Russia official exchange rate: 68.84"
    )
    if user.current_address:
        text = (
            f"⚠️ If you want to get a new address then"
            "first update the status of the current one! ⚠️"
        )
    await callback.bot.send_message(
        callback.from_user.id, text,
        reply_markup=get_info_keyboard(bool(user.current_address)),
        parse_mode='Markdown')
    await callback.bot.delete_message(
        callback.message.chat.id, callback.message.message_id
    )


async def get_addresses(callback: types.CallbackQuery):
    _, status, current_page = callback.data.split('#')
    data = await addresses_api.get_addresses(status)
    addresses = addresses_api.serialize_addresses(data)
    keyboard = get_list_of_addresses(addresses, int(current_page), status)
    await callback.bot.send_message(
        callback.from_user.id, f"Адреса **{status}**\n`page: {current_page}`",
        reply_markup=keyboard, parse_mode='Markdown'
    )
    await callback.bot.delete_message(
        callback.message.chat.id, callback.message.message_id
    )


async def get_address(callback: types.CallbackQuery):
    address_id = callback.data.split('#')[1]
    data = await addresses_api.get_address(address_id)
    address_data = addresses_api.serialize_addresses(data)
    text = (
        "⬇️ Your shipping address ⬇️\n"
        f"**Name**: `{address_data.name}`\n"
        f"__Line 1__: `{address_data.line_1}`\n"
        f"__Line 2__: `{address_data.line_2}`\n"
        f"**City**: `{address_data.city}`\n"
        f"**State**: `{address_data.state}`\n"
        f"**ZIP**: `{address_data.zip_code}`\n"
        f"**Phone number**: `{address_data.phone}`\n\n"
    )
    if address_data.using_now:
        text += f"This address now using"

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

def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start", "menu"], state="*")
    dp.register_callback_query_handler(
        back_to_menu, lambda callback: callback.data == 'menu')
    dp.register_callback_query_handler(
        get_profile, lambda callback: callback.data == 'menu#profile', state="*")
    dp.register_callback_query_handler(
        get_info, lambda callback: callback.data == 'menu#get_info', state="*")
    dp.register_callback_query_handler(
        get_addresses, lambda callback: callback.data.split('#')[0] == 'addresses')
