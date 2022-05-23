from aiogram import Dispatcher, types

from settings.settings import DEFAULT_COMMANDS


async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            types.BotCommand(command, description)
            for command, description in DEFAULT_COMMANDS
        ]
    )
