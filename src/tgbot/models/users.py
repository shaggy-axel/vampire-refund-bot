from typing import NamedTuple


class UserTuple(NamedTuple):
    telegram_id: int
    username: str
    using_now: bool
    current_address: int
