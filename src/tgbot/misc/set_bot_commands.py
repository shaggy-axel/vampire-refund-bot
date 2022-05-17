from aiogram import Dispatcher, types


async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("menu", "Output menu"),
            types.BotCommand("start", "Sign up"),
        ]
    )
