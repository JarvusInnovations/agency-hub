import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(BASE_DIR / "credentials.json")
config = {
    **os.environ,
}

SECRET_KEY = config["SECRET_KEY"]
METABASE_SECRET_KEY = config["METABASE_SECRET_KEY"]

# Build paths inside the project like this: BASE_DIR / 'subdir'.

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    # django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # thrid party
    "mailer",
    # this app
    "user",
    "agency",
    "metabase",
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

ROOT_URLCONF = "main.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "main.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config.get("POSTGRES_NAME"),
        "USER": config.get("POSTGRES_USER"),
        "PASSWORD": config.get("POSTGRES_PASSWORD"),
        "HOST": config.get("POSTGRES_HOST", "db"),
        # "NAME": "agency-hub",
        # "USER": "postgres",
        # "PASSWORD": "postgres",
        # "HOST": "127.0.0.1",
        "PORT": 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
AUTH_USER_MODEL = "user.User"

_dpv = "django.contrib.auth.password_validation"
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": f"{_dpv}.UserAttributeSimilarityValidator"},
    {"NAME": f"{_dpv}.MinimumLengthValidator"},
    {"NAME": f"{_dpv}.CommonPasswordValidator"},
    {"NAME": f"{_dpv}.NumericPasswordValidator"},
]

# Django registration
ACCOUNT_ACTIVATION_DAYS = 30

# Email
EMAIL_BACKEND = "mailer.backend.DbBackend"

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]


UNREST_STRING_TYPES = [
    "ULID",
]

METABASE_SITE_URL = "http://dashboards.calitp.org"
