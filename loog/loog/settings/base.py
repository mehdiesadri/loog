"""
Django settings for loog project.

Generated by 'django-admin startproject' using Django 3.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

from celery.schedules import crontab
import loog.tasks

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "this-is-not-secure!")

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    # Project's Apps
    "core.apps.CoreConfig",
    "main.apps.MainConfig",
    "accounts.apps.AccountsConfig",
    "discovery.apps.DiscoveryConfig",
    "chat.apps.ChatConfig",
    # Third-Party Apps
    "channels",
    "crispy_forms",
    "rest_framework"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "loog.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates', ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "loog.wsgi.application"
ASGI_APPLICATION = "loog.routing.application"

CRISPY_TEMPLATE_PACK = "bootstrap4"

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

SITE_ID = 1

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
}

MESSAGES_TO_LOAD = 15

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Collect static files here
STATIC_ROOT = "/usr/apps/loog/static/"
STATIC_URL = "/static/"

# Collect media files here
MEDIA_ROOT = "/usr/apps/loog/media/"
MEDIA_URL = "/media/"

# look for static assets here
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Login and Logout
LOGIN_URL = "accounts:login"
LOGOUT_URL = "accounts:logout"
LOGIN_REDIRECT_URL = "main:homepage"
LOGOUT_REDIRECT_URL = "accounts:login"
PASSWORD_RESET_TIMEOUT_DAYS = 1

# OAuth
AUTHLIB_OAUTH_CLIENTS = {
    'google': {
        'client_id': '149707931788-pa3njrbturb8u6d9nshh9asja7p04mlg.apps.googleusercontent.com',
        'client_secret': 'pGv_qh9wgFW9YNDnVnEwNvP-'
    }
}


# Celery
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
CELERY_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}"
CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}"

# Celery heart beat
CELERY_BEAT_SCHEDULE = {
    "sample_task": {
        "task": "loog.tasks.debug_task",
        "schedule": crontab(minute="*/1"),
    },
}

# SMTP
DEFAULT_FROM_EMAIL = 'loogtest0@gmail.com'
