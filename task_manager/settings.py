import os
from pathlib import Path

from dotenv import load_dotenv
import dj_database_url


load_dotenv()

SECRET_KEY = os.getenv("TASK_MANAGER_SECRET_KEY")
DEBUG = os.getenv("DEBUG_STATUS", False)

BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "webserver", "siderai-tm.herokuapp.com"]

INTERNAL_IPS = [
    "127.0.0.1",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd party
    "rest_framework",
    "drf_yasg",
    # local
    "task_manager",
    "task_manager.tasks",
    "task_manager.users",
    "task_manager.statuses",
    "task_manager.labels",
    "task_manager.api",
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

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ]
}

ROOT_URLCONF = "task_manager.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "task_manager.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


db_from_env = dj_database_url.config(conn_max_age=0, ssl_require=False)
if db_from_env:
    DATABASES["default"] = db_from_env


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
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


LOGIN_URL = "/login/"

LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "UTC"
DATETIME_FORMAT = "d-m-Y H:i"
USE_I18N = True
USE_L10N = False
USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
