import json
import os
from pathlib import Path


# TELEGRAM BOT
BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMINS = tuple(map(int, os.environ.get("ADMINS", "123456").split(',')))
GROUP_ID = os.environ.get("GROUP_ID", "-543210")

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

# Backend Settings
BASE_DIR = Path(__file__).resolve().parent.parent
BASE_API = "http://web:8000/api/v1/"
SECRET_KEY = os.environ.get("SECRET_KEY", "super30r2jsecretjfi02keyfj-")
DEBUG = bool(os.environ.get("DEBUG"))
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(',')

# SPOOFER
SPOOFER_SETTINGS = {}
spoofer_settings_file = os.path.join(BASE_DIR, "spoofer-settings.json")
with open(spoofer_settings_file, 'r') as file:
    SPOOFER_SETTINGS = json.load(file)

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'django_filters',

    'apps.addresses',
    'apps.users',
    'apps.products',
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

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = 'static'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
