from settings import settings as consts
from settings.data import CacheConfig, Config, TgBot, Miscellaneous


def load_config() -> Config:
    """ load config with telegram-bot, database and extra fields """
    return Config(
        tg_bot=TgBot(
            token=consts.BOT_TOKEN, admin_ids=consts.ADMINS
        ),
        cache_config=CacheConfig(
            host=consts.REDIS_HOST,
            port=consts.REDIS_PORT,
            password=consts.REDIS_PASSWORD
        ),
        misc=Miscellaneous()
    )
