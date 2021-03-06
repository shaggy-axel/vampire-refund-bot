from aiogram import types, dispatcher

from tgbot.handlers.user import get_profile
from tgbot.keyboards.inline import get_info_keyboard
from tgbot.services import addresses_api, telegram_user_api
from settings.text import BUTTONS_TEXT, MESSAGE_TEXT


async def get_info(message: types.Message, state: dispatcher.FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
    data = telegram_user_api.get_user(message.from_user.id)
    user = telegram_user_api.serialize_user(data)
    text = MESSAGE_TEXT["GET_INFO_IF_HAVE_NO_ADDRESS"].format(
        first_name=message.from_user.first_name)

    if user.current_address:
        text = MESSAGE_TEXT["GET_INFO_IF_HAVE_ADDRESS"]

    await message.bot.send_message(
        message.from_user.id, text,
        reply_markup=get_info_keyboard(bool(user.current_address)),
        parse_mode='Markdown')
    await message.bot.delete_message(message.chat.id, message.message_id)


async def get_address(callback: types.CallbackQuery, state: dispatcher.FSMContext):
    data = addresses_api.get_new_address(country=callback.data.split(':')[1])
    addresses = addresses_api.serialize_addresses(data)
    telegram_user_api.use_address(callback.from_user, addresses.id)

    callback.message.from_user = callback.from_user
    await get_profile(callback.message, state)


def register_address(dp: dispatcher.Dispatcher):
    dp.register_message_handler(
        get_info, lambda message: BUTTONS_TEXT['GET_INFO'] in message.text, state="*")
    dp.register_callback_query_handler(
        get_address, lambda callback: callback.data.split(':')[0] == 'get_address')
