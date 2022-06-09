from aiogram import dispatcher, types
from settings.text import ADDRESS_FORM_TEXT
from tgbot.keyboards.inline import get_countries

from tgbot.misc.states import AddressForm
from tgbot.services import addresses_api


async def save_name_go_to_line_1(message: types.Message, state: dispatcher.FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await AddressForm.next()
    await message.bot.send_message(
        message.from_user.id, ADDRESS_FORM_TEXT["ASK_FOR_LINE_1"],
        parse_mode="Markdown")


async def save_line_1_go_to_line_2(message: types.Message, state: dispatcher.FSMContext):
    async with state.proxy() as data:
        data['line_1'] = message.text
    await AddressForm.next()
    await message.bot.send_message(
        message.from_user.id, ADDRESS_FORM_TEXT["ASK_FOR_LINE_2"],
        parse_mode="Markdown")


async def save_line_2_go_to_city(message: types.Message, state: dispatcher.FSMContext):
    async with state.proxy() as data:
        data['line_2'] = message.text
    await AddressForm.next()
    await message.bot.send_message(
        message.from_user.id, ADDRESS_FORM_TEXT["ASK_FOR_CITY"],
        parse_mode="Markdown")


async def save_city_go_to_state(message: types.Message, state: dispatcher.FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
    await AddressForm.next()
    await message.bot.send_message(
        message.from_user.id, ADDRESS_FORM_TEXT["ASK_FOR_STATE"],
        parse_mode="Markdown")


async def save_state_go_to_zip_code(message: types.Message, state: dispatcher.FSMContext):
    async with state.proxy() as data:
        data['state'] = message.text
    await AddressForm.next()
    await message.bot.send_message(
        message.from_user.id, ADDRESS_FORM_TEXT["ASK_FOR_ZIP_CODE"],
        parse_mode="Markdown")


async def save_zip_code_go_to_phone(message: types.Message, state: dispatcher.FSMContext):
    async with state.proxy() as data:
        data['zip_code'] = message.text
    await AddressForm.next()
    await message.bot.send_message(
        message.from_user.id, ADDRESS_FORM_TEXT["ASK_FOR_PHONE"],
        parse_mode="Markdown")


async def save_phone_go_to_country(message: types.Message, state: dispatcher.FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await AddressForm.next()
    await message.bot.send_message(
        message.from_user.id, ADDRESS_FORM_TEXT["ASK_FOR_COUNTRY"],
        reply_markup=get_countries(), parse_mode="Markdown")


async def save_country_finish(callback: types.CallbackQuery, state: dispatcher.FSMContext):
    async with state.proxy() as data:
        data['country'] = callback.data.split(':')[1]
        addresses_api.create_address({
            'name': data['name'],
            'line_1': data['line_1'],
            'line_2': data['line_2'],
            'city': data['city'],
            'state': data['state'],
            'zip_code': data['zip_code'],
            'phone': data['phone'],
            'country': data['country'],
        })
    await state.finish()
    await callback.bot.send_message(
        callback.from_user.id, ADDRESS_FORM_TEXT["FINISH"],
        parse_mode="Markdown")


def register_address_states(dp: dispatcher.Dispatcher):
    dp.register_message_handler(save_name_go_to_line_1, state=AddressForm.name)
    dp.register_message_handler(save_line_1_go_to_line_2, state=AddressForm.line_1)
    dp.register_message_handler(save_line_2_go_to_city, state=AddressForm.line_2)
    dp.register_message_handler(save_city_go_to_state, state=AddressForm.city)
    dp.register_message_handler(save_state_go_to_zip_code, state=AddressForm.state)
    dp.register_message_handler(save_zip_code_go_to_phone, state=AddressForm.zip_code)
    dp.register_message_handler(save_phone_go_to_country, state=AddressForm.phone)
    dp.register_callback_query_handler(save_country_finish, state=AddressForm.country)
