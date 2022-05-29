from settings import settings as consts
from settings.data import Config, TgBot, Miscellaneous


def load_config() -> Config:
    """ load config with telegram-bot, database and extra fields """
    return Config(
        tg_bot=TgBot(
            token=consts.BOT_TOKEN, admin_ids=consts.ADMINS
        ),
        misc=Miscellaneous()
    )
