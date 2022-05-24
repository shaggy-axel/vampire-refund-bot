import os
from pathlib import Path


# TELEGRAM BOT
BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMINS = tuple(map(int, os.environ.get("ADMINS", "").split(',')))
USE_REDIS = bool(os.environ.get("USE_REDIS"))
MESSAGE_TEXT = {
    "START_COMMAND": "Автоматическая выдача чистых адресов в США и странах Европы.",
    "MENU_COMMAND": "Пожалуйста, выберите действие.",
    "GET_CONTACTS_COMMAND": "*Админ:* @RefBanker\n*Скупщик:* @RefBank\_Buyer\n*Поддержка бота:* @dexedrine",

    "PROFILE_IF_HAVE_NO_ADDRESS": "У вас нет используемых адресов!\nПожалуйста, нажмите *Получить адрес* для начала работы.",
    "PROFILE_IF_HAVE_ADDRESS": (
        "*Name:* {address_name}\n"
        "*Line 1:* {address_line_1}\n"
        "*Line 2:* {address_line_2}\n"
        "*City:* {address_city}\n"
        "*State:* {address_state}\n"
        "*ZIP:* {address_zip_code}\n"
        "*Phone number:* {address_phone}\n\n"
        "*Пожалуйста, изменяйте статус адреса только после заказа!*"
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
    "GET_INFO": "🏚️ Получить адрес",
    "PROFILE": "👤 Профиль",
    "CONTACTS": "📘 FAQ",

    "CHANGE_STATUS": "Адрес использован",
    "GET_INFO_OK": "🇺🇸 США",
    "GET_INFO_NO_THANKS": "🇨🇿 Чехия",
    "STATUS_USED": '✅ Основной товар отправлен',
    "STATUS_HOLD": '😡 Нужен новый адрес',
}

DEFAULT_COMMANDS = [
    # (command, description),
    ("start", "Sign up"),
    ("menu", "Output menu"),
]

# DATABASE
POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASS = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_HOST = "db"
POSTGRES_PORT = 5432

# REDIS
REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = int(os.environ.get('REDIS_PORT'))
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')

# Backend Settings
BASE_DIR = Path(__file__).resolve().parent.parent
BASE_API = "http://web:8000/api/v1/"
SECRET_KEY = os.environ.get("SECRET_KEY", "super30r2jsecretjfi02keyfj-")
DEBUG = bool(os.environ.get("DEBUG"))
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(',')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'apps.addresses',
    'apps.users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': POSTGRES_DB,
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASS,
        'HOST': POSTGRES_HOST,
        'PORT': POSTGRES_PORT,
        'ATOMIC_REQUESTS': True,
    },
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
