from aiogram import dispatcher, types

from tgbot.misc.states import ProductForm
from tgbot.keyboards.inline import (
    cancel_button, get_status_keyboard, pass_button, profile_keyboard)
from tgbot.services import addresses_api, telegram_user_api
from settings.text import BUTTONS_TEXT, MESSAGE_TEXT, PRODUCT_FORM_TEXT
from tgbot.services.utils import get_user_group_status


async def get_profile(message: types.Message, state: dispatcher.FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
    data = telegram_user_api.get_user(message.from_user.id)
    user = telegram_user_api.serialize_user(data)

    if user.current_address:
        data = addresses_api.get_address_info(user.current_address)
        address = addresses_api.serialize_addresses(data)
        text = MESSAGE_TEXT["PROFILE_IF_HAVE_ADDRESS"].format(
            address_name=address.name,
            address_line_1=address.line_1, address_line_2=address.line_2,
            address_city=address.city, address_state=address.state,
            address_zip_code=address.zip_code, address_phone=address.phone
        )
    else:
        text = MESSAGE_TEXT["PROFILE_IF_HAVE_NO_ADDRESS"]

    await message.bot.send_message(
        message.from_user.id, text, parse_mode="Markdown",
        reply_markup=profile_keyboard(bool(user.current_address)))
    await message.delete()


async def change_status_choice(callback: types.CallbackQuery):
    keyboard = get_status_keyboard()
    text = MESSAGE_TEXT["CHOICES_STATUS_FOR_ADDRESS"]
    await callback.bot.send_message(
        callback.from_user.id, text, reply_markup=keyboard, parse_mode="Markdown")
    await callback.bot.delete_message(callback.from_user.id, callback.message.message_id)


async def change_status_send(callback: types.CallbackQuery, state: dispatcher.FSMContext):
    status = callback.data.split('#')[1]
    if status != "hold":
        async with state.proxy() as data:
            data['status'] = status
            data['user'] = callback.from_user

        await ProductForm.first()
        keyboard = types.InlineKeyboardMarkup()
        await callback.bot.send_message(
            callback.from_user.id, PRODUCT_FORM_TEXT['ASK_FOR_TRACK_NUMBER'],
            reply_markup=keyboard.add(
                pass_button(BUTTONS_TEXT["HAVE_NO_TRACK_NUMBER"], "pass_track"),
                cancel_button("????????????????")
            ),
            parse_mode="Markdown")
        await callback.bot.delete_message(callback.from_user.id, callback.message.message_id)
        return

    # change status
    user_data = telegram_user_api.get_user(callback.from_user.id)
    user = telegram_user_api.serialize_user(user_data)
    user_in_group = await get_user_group_status(callback.bot, user.telegram_id)
    address_data = addresses_api.change_status(
        address_id=user.current_address, status=status,
        user_in_group=user_in_group)

    # get new address
    data = addresses_api.get_new_address(country=address_data['country'])
    addresses = addresses_api.serialize_addresses(data)
    telegram_user_api.use_address(callback.from_user, addresses.id)

    callback.message.from_user = callback.from_user
    await get_profile(callback.message, state)


def register_user(dp: dispatcher.Dispatcher):
    dp.register_message_handler(
        get_profile, lambda message: BUTTONS_TEXT['PROFILE'] in message.text, state="*")
    dp.register_callback_query_handler(
        change_status_choice, lambda callback: 'change_status' == callback.data)
    dp.register_callback_query_handler(
        change_status_send, lambda callback: 'status' == callback.data.split('#')[0], state="*")
