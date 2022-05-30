from datetime import datetime
import logging
from typing import Union
from aiogram import types, dispatcher
from settings.text import PRODUCT_FORM_TEXT
from tgbot.keyboards.inline import time_choice_keyboard

from tgbot.misc.states import ProductForm
from tgbot.keyboards.calendar_keyboard import SimpleCalendar


async def cancel_handler(
    _: Union[types.Message, types.CallbackQuery],
    state: dispatcher.FSMContext
) -> None:
    """ Allow user to cancel any action """
    logging.info('ПЫТАЕТСЯ ОТМЕНИТЬ!!')
    current_state = await state.get_state()
    if current_state is None:
        await _.bot.send_message(_.from_user.id, "Нечего отменять")
        return

    await _.bot.send_message(_.from_user.id, "Отменено")
    await state.finish()


async def save_product_name_go_to_shop_name(
    message: types.Message, state: dispatcher.FSMContext
):
    await message.bot.send_message(message.from_user.id, 'получил')
    async with state.proxy() as data:
        data['product_name'] = message.text
    
    await ProductForm.next()
    await message.answer(
        PRODUCT_FORM_TEXT["ASK_FOR_SHOP_NAME"], parse_mode="Markdown")


async def save_shop_name_go_to_price(
    message: types.Message, state: dispatcher.FSMContext
):
    async with state.proxy() as data:
        data['shop_name'] = message.text

    await ProductForm.next()
    await message.answer(
        PRODUCT_FORM_TEXT["ASK_FOR_PRICE"], parse_mode="Markdown")


async def save_price_go_to_delivery_date(
    message: types.Message, state: dispatcher.FSMContext
):
    async with state.proxy() as data:
        data['price'] = message.text

    await ProductForm.next()
    keyboard = await SimpleCalendar().start_calendar()
    await message.answer(
        PRODUCT_FORM_TEXT["ASK_FOR_DATE"], reply_markup=keyboard,
        parse_mode="Markdown")


async def save_delivery_date_go_to_delivery_time(
    callback: types.CallbackQuery, state: dispatcher.FSMContext
):
    selected, date = await SimpleCalendar().process_selection(callback, callback.data)
    if not selected:
        return

    async with state.proxy() as data:
        data['delivery_date'] = date

    await ProductForm.next()

    keyboard = time_choice_keyboard()
    await callback.bot.send_message(
        callback.from_user.id,
        PRODUCT_FORM_TEXT["ASK_FOR_TIME"],
        reply_markup=keyboard, parse_mode="Markdown"
    )


async def save_delivery_time_and_finish(
    callback: types.CallbackQuery, state: dispatcher.FSMContext
):
    async with state.proxy() as data:
        data['delivery_time'] = callback.data
        delivery_date = datetime(
            data['delivery_date'].year, data['delivery_date'].month,
            data['delivery_date'].day, int(data['delivery_time'].split(':')[0]),
            int(data['delivery_time'].split(':')[1]), 0
        )

        reply = (
            f"*{data['product_name']}* from _{data['shop_name']}_\n"
            f"price: `{data['price']}`\n"
            f"delivery date: `{delivery_date}`\n"
            # f"address status: {}"
        )

    await state.finish()
    await callback.bot.send_message(
        callback.from_user.id, reply, parse_mode="Markdown"
    )


def register_states(dp: dispatcher.Dispatcher):
    logging.info("ЗАРЕГИСТРИРОВАЛ СТЕЙТЫ")
    dp.message_handler(cancel_handler, commands='cancel', state='*')
    dp.message_handler(
        cancel_handler, lambda message: message.text.lower() == "cancel", state='*')
    dp.register_callback_query_handler(
        cancel_handler, lambda callback: callback.data.lower() == "cancel", state="*")

    dp.register_message_handler(
        save_product_name_go_to_shop_name,
        lambda _: True,
        state=ProductForm.product_name)
    dp.register_message_handler(
        save_shop_name_go_to_price,
        lambda _: True,
        state=ProductForm.shop_name)
    dp.register_message_handler(
        save_price_go_to_delivery_date,
        lambda _: True,
        state=ProductForm.price)
    dp.register_callback_query_handler(
        save_delivery_date_go_to_delivery_time,
        lambda _: True,
        state=ProductForm.delivery_date)
    dp.register_callback_query_handler(
        save_delivery_time_and_finish,
        lambda _: True,
        state=ProductForm.delivery_time)
