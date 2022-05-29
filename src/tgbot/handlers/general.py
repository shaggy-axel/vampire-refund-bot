from aiogram import types, Dispatcher

from settings.text import MESSAGE_TEXT, BUTTONS_TEXT


async def get_contacts(message: types.Message):
    text = MESSAGE_TEXT["GET_CONTACTS_COMMAND"]
    await message.bot.send_message(
        message.from_user.id, text, parse_mode="Markdown",
    )
    await message.bot.delete_message(
        message.from_user.id, message.message_id
    )


def register_general(dp: Dispatcher):
    dp.register_message_handler(
        get_contacts, lambda message: BUTTONS_TEXT['CONTACTS'] in message.text)
