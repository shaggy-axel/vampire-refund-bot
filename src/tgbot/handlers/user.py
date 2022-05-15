from aiogram import Dispatcher, types

from tgbot.keyboards.inline import menu_keyboard
from tgbot.services.telegram_user_api import sign_up_user


async def user_start(message: types.Message):
    text = "some menu text"
    if "start" in message.get_command():
        text = "some welcome text\n" + text
        await sign_up_user(message.from_user)

    keyboard = menu_keyboard()
    await message.reply(text, reply_markup=keyboard)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start", "menu"], state="*")
