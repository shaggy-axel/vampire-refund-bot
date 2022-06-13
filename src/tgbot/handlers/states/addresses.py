from aiogram import dispatcher, types
from settings.text import ADDRESS_FORM_TEXT
from tgbot.keyboards.inline import cancel_button, cancel_keyboard, get_countries, spoof_or_save_button

from tgbot.misc.states import AddressForm
from tgbot.services import addresses_api
from tgbot.services.spoofer import generate_spoofing_addresses


async def save_name_go_to_street(message: types.Message, state: dispatcher.FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await AddressForm.next()
    await message.bot.send_message(
        message.from_user.id, ADDRESS_FORM_TEXT["ASK_FOR_STREET"], reply_markup=cancel_keyboard("Отменить"),
        parse_mode="Markdown")


async def save_street_go_to_house(message: types.Message, state: dispatcher.FSMContext):
    async with state.proxy() as data:
        data['street'] = message.text
    await AddressForm.next()
    await message.bot.send_message(
        message.from_user.id, ADDRESS_FORM_TEXT["ASK_FOR_HOUSE"],
        parse_mode="Markdown", reply_markup=cancel_keyboard("Отменить"))


async def save_house_go_to_apartments(message: types.Message, state: dispatcher.FSMContext):
    async with state.proxy() as data:
        data['house'] = message.text
    await AddressForm.next()
    await message.bot.send_message(
        message.from_user.id, ADDRESS_FORM_TEXT["ASK_FOR_APART"],
        parse_mode="Markdown", reply_markup=cancel_keyboard("Отменить"))


async def save_apartments_go_to_city(message: types.Message, state: dispatcher.FSMContext):
    async with state.proxy() as data:
        data['apartments'] = message.text
    await AddressForm.next()
    await message.bot.send_message(
        message.from_user.id, ADDRESS_FORM_TEXT["ASK_FOR_CITY"],
        parse_mode="Markdown", reply_markup=cancel_keyboard("Отменить"))


async def save_city_go_to_state(message: types.Message, state: dispatcher.FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
    await AddressForm.next()
    await message.bot.send_message(
        message.from_user.id, ADDRESS_FORM_TEXT["ASK_FOR_STATE"],
        parse_mode="Markdown", reply_markup=cancel_keyboard("Отменить"))


async def save_state_go_to_zip_code(message: types.Message, state: dispatcher.FSMContext):
    async with state.proxy() as data:
        data['state'] = message.text
    await AddressForm.next()
    await message.bot.send_message(
        message.from_user.id, ADDRESS_FORM_TEXT["ASK_FOR_ZIP_CODE"],
        parse_mode="Markdown", reply_markup=cancel_keyboard("Отменить"))


async def save_zip_code_go_to_phone(message: types.Message, state: dispatcher.FSMContext):
    async with state.proxy() as data:
        data['zip_code'] = message.text
    await AddressForm.next()
    await message.bot.send_message(
        message.from_user.id, ADDRESS_FORM_TEXT["ASK_FOR_PHONE"],
        parse_mode="Markdown", reply_markup=cancel_keyboard("Отменить"))


async def save_phone_go_to_country(message: types.Message, state: dispatcher.FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await AddressForm.next()
    await message.bot.send_message(
        message.from_user.id, ADDRESS_FORM_TEXT["ASK_FOR_COUNTRY"],
        reply_markup=get_countries().add(cancel_button("Отменить")), parse_mode="Markdown")


async def save_country_finish(callback: types.CallbackQuery, state: dispatcher.FSMContext):
    async with state.proxy() as data:
        data['country'] = callback.data.split(':')[1]
        addresses_api.create_address({
            'name': data['name'],
            'line_1': data['street'],
            'line_2': f"{data['house']}/{data['apartments']}",
            'city': data['city'],
            'state': data['state'],
            'zip_code': data['zip_code'],
            'phone': data['phone'],
            'country': data['country'],
        })

    await callback.bot.send_message(
        callback.from_user.id, ADDRESS_FORM_TEXT["SPOOF_OR_SAVE"], reply_markup=spoof_or_save_button(),
        parse_mode="Markdown")
    await callback.bot.delete_message(callback.from_user.id, callback.message.message_id)


async def spoof_or_save(callback: types.CallbackQuery, state: dispatcher.FSMContext):
    if callback.data.split(":")[1] == "spoof":
        async with state.proxy() as data:
            spoof_data = {
                'name': data['name'],
                'street': data['street'],
                'house': data['house'],
                'apartments': data['apartments'],
                'city': data['city'],
                'state': data['state'],
                'zip_code': data['zip_code'],
                'phone': data['phone'],
                'country': data['country'],
            }
            addresses = generate_spoofing_addresses(spoof_data)
            for address in addresses:
                addresses_api.create_address({
                    'name': address['name'],
                    'line_1': address['street'],
                    'line_2': f"{address['house']} {address['apartments']}",
                    'city': address['city'],
                    'state': address['state'],
                    'zip_code': address['zip_code'],
                    'phone': address['phone'],
                    'country': address['country'],
                })

    await state.finish()
    await callback.bot.send_message(
        callback.from_user.id, ADDRESS_FORM_TEXT["FINISH"],
        parse_mode="Markdown")
    await callback.bot.delete_message(callback.from_user.id, callback.message.message_id)


def register_address_states(dp: dispatcher.Dispatcher):
    dp.register_message_handler(save_name_go_to_street, state=AddressForm.name)
    dp.register_message_handler(save_street_go_to_house, state=AddressForm.street)
    dp.register_message_handler(save_house_go_to_apartments, state=AddressForm.house)
    dp.register_message_handler(save_apartments_go_to_city, state=AddressForm.apartments)
    dp.register_message_handler(save_city_go_to_state, state=AddressForm.city)
    dp.register_message_handler(save_state_go_to_zip_code, state=AddressForm.state)
    dp.register_message_handler(save_zip_code_go_to_phone, state=AddressForm.zip_code)
    dp.register_message_handler(save_phone_go_to_country, state=AddressForm.phone)
    dp.register_callback_query_handler(
        save_country_finish, lambda cb: cb.data.split(':')[0] == "create_address", state=AddressForm.country)
    dp.register_callback_query_handler(
        spoof_or_save, lambda cb: cb.data.split(':')[0] == "spoof_address", state=AddressForm.country)
