from aiogram import dispatcher, types

from settings.text import BUTTONS_TEXT
from tgbot.services import addresses_api

async def orders(message: types.Message, state: dispatcher.FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()

    addresses = addresses_api.serialize_addresses(addresses_api.get_used_addresses())
    text = "\n".join([
        (
            f"Name: {address.name}\n"
            f"Line 1: {address.line_1}\n"
            f"Line 2: {address.line_2}\n"
            f"City: {address.city}\n"
            f"State: {address.state}\n"
            f"Zip Code: {address.zip_code}\n"
            f"Phone: {address.phone}\n"
            f"Status: {address.status}\n"
            f"Used By: {address.used_by}\n"
            f"Used At: {address.used_at}\n"
            f"Using Now: {address.using_now}\n"
            f"Country: {address.country}\n"
            f"User in Group Status: {address.user_in_group}\n"
        )
        for address in addresses
    ])

    await message.bot.send_message(message.from_user.id, text=text)


def register_admin(dp: dispatcher.Dispatcher):
    dp.register_message_handler(orders, text=BUTTONS_TEXT['ORDERS'], state="*")