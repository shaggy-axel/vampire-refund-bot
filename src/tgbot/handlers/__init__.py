from tgbot.handlers.user import register_user
from tgbot.handlers.address import register_address
from tgbot.handlers.menu import register_menu
from tgbot.handlers.general import register_general
from tgbot.handlers.states import register_states


__all__ = [
    "register_menu", "register_address", "register_user",
    "register_general", "register_states"
]
