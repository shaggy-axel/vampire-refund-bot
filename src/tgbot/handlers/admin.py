from aiogram import dispatcher, types

from settings.text import (
    ALL_INFO_IN_ORDER_PAGE, BUTTONS_TEXT, ADDRESS_FORM_TEXT, MESSAGE_TEXT)
from tgbot.keyboards.pagination import get_orders_keyboard, get_back_to_orders_keyboard
from tgbot.misc.states import AddressForm
from tgbot.services import addresses_api
from tgbot.services.utils import get_all_data_of_order


async def create_address(message: types.Message, state: dispatcher.FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()

    await AddressForm.name.set()

    await message.bot.send_message(
        message.from_user.id, ADDRESS_FORM_TEXT['ASK_FOR_NAME'], parse_mode='Markdown')


async def orders(message: types.Message, state: dispatcher.FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()

    keyboard = get_orders_keyboard()

    await message.bot.send_message(
        message.from_user.id, text=MESSAGE_TEXT["ORDERS"], reply_markup=keyboard)


async def orders_callback_change_page(callback: types.CallbackQuery):
    current_page = int(callback.data.split('#')[1])
    keyboard = get_orders_keyboard(current_page)

    await callback.bot.send_message(
        callback.from_user.id, text=MESSAGE_TEXT["ORDERS"], reply_markup=keyboard)
    await callback.bot.delete_message(
        callback.from_user.id, callback.message.message_id)


async def order_page(callback: types.CallbackQuery):
    _, address_id, current_page = callback.data.split('#')
    keyboard = get_back_to_orders_keyboard(address_id, current_page)

    all_data = get_all_data_of_order(int(address_id), callback.from_user)

    await callback.bot.send_message(
        callback.from_user.id,
        ALL_INFO_IN_ORDER_PAGE.format(**all_data).replace('_', '\_'),
        parse_mode="Markdown",
        reply_markup=keyboard)
    await callback.bot.delete_message(
        callback.from_user.id, callback.message.message_id)


async def delivered_address(callback: types.CallbackQuery):
    address_id = callback.data.split('#')[1]
    user_in_group = addresses_api.get_address_info(address_id)["user_in_group"]
    addresses_api.change_status(address_id, "delivered", user_in_group)
    await callback.bot.send_message(
        callback.from_user.id, MESSAGE_TEXT["AFTER_DELIVERED"], parse_mode="Markdown")
    await callback.bot.delete_message(
        callback.from_user.id, callback.message.message_id)


def register_admin(dp: dispatcher.Dispatcher):
    dp.register_message_handler(create_address, text=BUTTONS_TEXT['CREATE_ADDRESS'], state="*")
    dp.register_message_handler(orders, text=BUTTONS_TEXT['ORDERS'], state="*")
    dp.register_callback_query_handler(
        orders_callback_change_page,
        lambda callback: callback.data.split('#')[0] == 'orders', state="*")
    dp.register_callback_query_handler(
        order_page, lambda callback: callback.data.split('#')[0] == 'order', state="*")
    dp.register_callback_query_handler(
        delivered_address, lambda callback: callback.data.split('#')[0] == 'delivered',
        state="*",
    )

