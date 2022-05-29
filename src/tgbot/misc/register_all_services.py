from aiogram import Dispatcher
from tgbot.filters.admin import AdminFilter
from tgbot.handlers import register_user, register_menu, register_address, register_general
from tgbot.middlewares.db import DbMiddleware
from tgbot.misc.set_bot_commands import set_default_commands


def register_all_middlewares(dp: Dispatcher):
    dp.setup_middleware(DbMiddleware())


def register_all_filters(dp: Dispatcher):
    dp.filters_factory.bind(AdminFilter)


def register_all_handlers(dp: Dispatcher):
    register_user(dp)
    register_menu(dp)
    register_address(dp)
    register_general(dp)


async def register_all_services(dp: Dispatcher):
    register_all_middlewares(dp)
    register_all_filters(dp)
    register_all_handlers(dp)
    await set_default_commands(dp)
