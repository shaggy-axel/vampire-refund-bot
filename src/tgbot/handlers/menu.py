from aiogram import types, Dispatcher

from settings.text import MESSAGE_TEXT
from tgbot.services import telegram_user_api
from tgbot.keyboards.reply import menu_keyboard


async def back_to_menu(callback: types.CallbackQuery):
    callback.message.from_user.id = callback.from_user.id
    await menu(callback.message)


async def menu(message: types.Message):
    text = MESSAGE_TEXT["START_COMMAND"]

    if not message.get_command():
        pass
    elif "start" in message.get_command():
        text = MESSAGE_TEXT["MENU_COMMAND"]
        telegram_user_api.sign_up_user(message.from_user)

    keyboard = menu_keyboard(is_admin=telegram_user_api.is_admin(message.from_user))
    await message.bot.send_message(
        message.from_user.id, text,
        reply_markup=keyboard, parse_mode="Markdown")
    await message.bot.delete_message(message.chat.id, message.message_id)


def register_menu(dp: Dispatcher):
    dp.register_message_handler(menu, commands=["start", "menu"])
    dp.register_callback_query_handler(
        back_to_menu, lambda callback: callback.data == 'menu')
