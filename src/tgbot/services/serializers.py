from typing import Union

from tgbot.models import UserTuple


def serialize_user(data: Union[dict, list[dict]]) -> Union[UserTuple, list[UserTuple]]:
    if isinstance(data, dict):
        return UserTuple(
            telegram_id=data['telegram_id'],
            username=data['username'],
            using_now=data['using_now'],
            current_address=data['current_address'],
        )
    elif isinstance(data, list):
        return [
            UserTuple(
                telegram_id=user['telegram_id'],
                username=user['username'],
                using_now=user['using_now'],
                current_address=user['current_address'],
            )
            for user in data
        ]
    raise TypeError(str(data))
