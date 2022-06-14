from emoji import emojize

from settings import settings


COUNTRY_DISPLAY = {
    settings.USA_CODE: emojize(":United_States: USA"),
    settings.UK_CODE: emojize(":United_Kingdom: UK"),
    settings.CZ_CODE: emojize(":Czechia: CZ"),
}

MESSAGE_TEXT = {
    "START_COMMAND": "Пожалуйста, выберите действие.",
    "MENU_COMMAND": "Пожалуйста, выберите действие.",
    "GET_CONTACTS_COMMAND": "Используя сервис, вы подтверждаете, что согласны с процентами по выплате, указанными в нашем [скуп-листе](https://docs.google.com/spreadsheets/d/1_vRXD4fowadQ3GF4aPJHjd8NEjEEMwvNeGSIxD0wbqI/edit#gid=0).\n\n*Админ:* @RefBanker\n*Скупщик:* @RefBank\_Buyer\n*Поддержка бота:* @dexedrine",

    "PROFILE_IF_HAVE_NO_ADDRESS": "У вас нет используемых адресов!\nПожалуйста, нажмите *Получить адрес* для начала работы.",
    "PROFILE_IF_HAVE_ADDRESS": (
        "*Name:* {address_name}\n"
        "*Line 1:* {address_line_1}\n"
        "*Line 2:* {address_line_2}\n"
        "*City:* {address_city}\n"
        "*State:* {address_state}\n"
        "*ZIP:* {address_zip_code}\n"
        "*Phone number:* {address_phone}\n\n"
        "⚡⚡⚡\n"
        "*Изменяйте статус адреса только после заказа основного товара, а не прогревочных!*"
    ),

    "GET_INFO_IF_HAVE_NO_ADDRESS": (
        "{first_name}, в какую страну будет отправлен товар?"
    ),
    "GET_INFO_IF_HAVE_ADDRESS": (
        "⚠️ Для получения нового адреса необходимо сначала изменить статус использования текущего!"
    ),

    "CHOICES_STATUS_FOR_ADDRESS": "✅ Адрес использован",
    "ORDERS": "Посылки:",
    "AFTER_DELIVERED": "✅ Статус успешно изменен!",
}

BUTTONS_TEXT = {
    "GET_INFO": "⭐ Получить адрес",
    "PROFILE": "👤 Профиль",
    "CONTACTS": "📘 FAQ",

    "CHANGE_STATUS": "✅ Адрес использован",
    "GET_INFO_OK": COUNTRY_DISPLAY,
    "GET_INFO_NO_THANKS": "No, thanks",
    "STATUS_USED": '✅ Succesful order!',
    "STATUS_HOLD": '😡 Hold / Ban / Suspend',


    "ORDERS": "📦 Посылки",
    "CREATE_ADDRESS": "➕ Добавить адрес",
    "DELIVERED": "Доставлено",
    "BACK_TO_ORDERS": "<- Посылки",
    "BACK_TO_MENU": "<<- Меню",
    "SPOOF_IT": "Спуфить",
    "SAVE_IT": "Сохранить адрес",
}

PRODUCT_FORM_TEXT = {
    "ASK_FOR_PRODUCT_NAME": "📦 Укажите наименование товара (например, MSI GeForce RTX 3080):",
    "ASK_FOR_SHOP_NAME": "🏬 Укажите название магазина (например, Amazon):",
    "ASK_FOR_PRICE": "💸 Укажите стоимость товара (например, 850$):",
    "ASK_FOR_PRODUCT_URL": "🔗 Отправьте ссылку на товар:",
    "ASK_FOR_PRODUCT_URL_AGAIN": "❌ Некорректная ссылка, отправьте ссылку на товар повторно!",
    "ASK_FOR_DATE": "📅 Выберите дату доставки:",
    "ASK_FOR_TIME": "⏲️ Выберите время доставки:",
    "FINISH": "💘 Спасибо за заказ! :3",
}

ADDRESS_FORM_TEXT = {
    "ASK_FOR_NAME": "Name:",
    "ASK_FOR_STREET": "Street:",
    "ASK_FOR_HOUSE": "House:",
    "ASK_FOR_APART": "Apartments:",
    "ASK_FOR_CITY": "City:",
    "ASK_FOR_STATE": "State:",
    "ASK_FOR_ZIP_CODE": "ZIP:",
    "ASK_FOR_PHONE": "Phone:",
    "ASK_FOR_COUNTRY": "Country:",
    "FINISH": "✅ Адрес сохранен!",
    "SPOOF_OR_SAVE": "Заспуфить 10 новых адресов или сохранить один?",
}

NOTIFY_TEXT_TO_ADMINS_ABOUT_USED_ADDRESS = (
    # user
    "*ID пользователя:* {user__telegram_id}\n"
    "*Имя пользователя:* {user__username}\n"
    "*Текущий адрес пользователя:* {user__current_address}\n"
    "*Статус в группе eBy PalPay:* {address__user_in_group}\n\n"

    # address
    "*ID адреса:* {address__id}\n"
    "*Имя дропа:* {address__name}\n"
    "*Страна:* {address__country}\n"
    "*Улица и номер дома:* {address__line_1}, {address__line_2}\n"
    "*Штат, город, индекс:* {address__city}, {address__state}, {address__zip_code}\n"
    "*Номер телефона:* {address__phone}\n"
    "*Адрес был использован:* {address__used_at}\n\n"

    # product
    "*Товар:* {product__name}\n"
    "*Магазин:* {product__shop_name}\n"
    "*Стоимость:* {product__price}\n"
    "*Дата доставки:* {product__delivery_date}\n"
    "*Ссылка:* {product__product_url}\n"
)

# change if you need to another text: string type
ALL_INFO_IN_ORDER_PAGE = NOTIFY_TEXT_TO_ADMINS_ABOUT_USED_ADDRESS
