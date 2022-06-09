from aiogram import Dispatcher

from tgbot.handlers.states.products import register_product_states
from tgbot.handlers.states.addresses import register_address_states


def register_states(dp: Dispatcher):
    register_product_states(dp)
    register_address_states(dp)
