from aiogram import Dispatcher, types

from tgbot.keyboards.inline import (
    get_info_keyboard, get_list_of_addresses, menu_keyboard)
from tgbot.services.telegram_user_api import sign_up_user
from tgbot.services import addresses_api


async def back_to_menu(callback: types.CallbackQuery):
    callback.message.from_user.id = callback.from_user.id
    await user_start(callback.message)


async def user_start(message: types.Message):
    text = "Please select an action"

    if not message.get_command():
        pass
    elif "start" in message.get_command():
        text = "Welcome!\n" + text
        await sign_up_user(message.from_user)

    keyboard = menu_keyboard()
    await message.bot.send_message(message.from_user.id, text, reply_markup=keyboard)
    await message.bot.delete_message(
        message.chat.id, message.message_id
    )



async def get_info(callback: types.CallbackQuery):
    text = (
        f"{callback.from_user.first_name}, please check our price. It's okay?\n\n"
        "Receive the parcel – $80\n"
        "CDEK ~ $25\n\n"
        "RU Bank of Russia official exchange rate: 68.84"
    )
    await callback.bot.send_message(
        callback.from_user.id, text, reply_markup=get_info_keyboard())
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


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start", "menu"], state="*")
    dp.register_callback_query_handler(
        back_to_menu, lambda callback: callback.data == 'menu')
    dp.register_callback_query_handler(
        get_info, lambda callback: callback.data == 'menu#get_info', state="*")
    dp.register_callback_query_handler(
        get_addresses, lambda callback: callback.data.split('#')[0] == 'addresses')
