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
        "*Пожалуйста, изменяйте статус адреса только после заказа основного товара, а не прогревочных!*"
    ),

    "GET_INFO_IF_HAVE_NO_ADDRESS": (
        "{first_name}, в какую страну будет отправлен товар?"
    ),
    "GET_INFO_IF_HAVE_ADDRESS": (
        "Для получения нового адреса необходимо сначала изменить статус использования текущего!"
    ),

    "CHOICES_STATUS_FOR_ADDRESS": "Адрес использован",
}

BUTTONS_TEXT = {
    "GET_INFO": "🏚 Получить адрес",
    "PROFILE": "👤 Профиль",
    "CONTACTS": "📘 FAQ",

    "CHANGE_STATUS": "Адрес использован",
    "GET_INFO_OK": "🇺🇸 США",
    "GET_INFO_NO_THANKS": "🇨🇿 Чехия",
    "STATUS_USED": '✅ Товар отправлен',
    "STATUS_HOLD": '😡 Нужен новый адрес',
}
