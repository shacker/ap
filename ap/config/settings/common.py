"""
Settings for athlete.photo project.

Django settings are documented at:
https://docs.djangoproject.com/en/dev/topics/settings/
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import environ
import pathlib
import sys


# Default directory locations (ie. can be overridden by more specific settings files)
ROOT_DIR = environ.Path(__file__) - 3  # (config/settings/base.py - 3 = root dir)
TMP_DIR = pathlib.Path("/tmp")
BASE_DIR = str(ROOT_DIR)  # Some apps, like django_extensions' `runscript` expect this to be set.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "ap",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
        "ATOMIC_REQUESTS": True,
    }
}

# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    # Default Django apps:
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admindocs",
    "django.contrib.postgres",
    # Template tags:
    "django.contrib.humanize",
    # Admin
    "django.contrib.admin",
]

THIRD_PARTY_APPS = [
    "django_extensions",
    "compressor",
    "captcha",
    "crispy_forms",
    "sorl.thumbnail",

    # Local or social logins
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.facebook",
    "allauth.socialaccount.providers.twitter",
]


LOCAL_APPS = [
    "ap.apps.contact",
    "ap.apps.core",
    "ap.apps.events",
    "ap.apps.faqs",
    "ap.apps.orgs",
    "ap.apps.photos",
    "ap.apps.users",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

DEBUG = False

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL = "noreply@athlete.photo"  # Override per-program?

ADMINS = [("Scot Hacker", "shacker@athlete.photo")]
MANAGERS = ADMINS

# Local time zone for this installation. Choices:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = "America/Los_Angeles"
USE_TZ = True

LANGUAGE_CODE = "en-us"

SITE_ID = 1

USE_I18N = False  # Per Django docs, no need for extra i18n/l10n machinery if
USE_L10N = False  # we're not using it *and* don't have locale middleware above.

LOCALE_PATHS = (str(ROOT_DIR) + "/locale",)

CSRF_USE_SESSIONS = False

# Use the mouse-based recaptcha from Google (django-recaptcha)
NOCAPTCHA = True

# Default template pack for CrispyForms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        "DIRS": [str(ROOT_DIR.path("templates"))],
        "OPTIONS": {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            "debug": DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]


# STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(ROOT_DIR.path("static"))]

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]

# This is where compiled/compressed files are output TO
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR("staticfiles"))

# Uploaded media
MEDIA_ROOT = str(ROOT_DIR("media"))
MEDIA_URL = "/media/"

# *.scss files linked with MIME type text/x-scss will be compiled to css by django-compressor
# React modules delivered with MIME type text/jsx will be compiled to webpack by django-compressor
SASS_COMMAND = "sassc {infile} {outfile}"
COMPRESS_PRECOMPILERS = (("text/x-scss", SASS_COMMAND),)
# COMPRESS_OFFLINE = True


# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = "ap.urls"
ADMIN_URL = r"^admin/"

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "ap.config.wsgi.application"

# PASSWORD STORAGE SETTINGS
# ------------------------------------------------------------------------------
# See https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
]


AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

# Custom user app defaults
AUTH_USER_MODEL = "users.User"
LOGIN_REDIRECT_URL = "home"
LOGIN_URL = "account_login"


# Allauth user/registration/signup/password/reset defaults. See:
# http://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_REQUIRED = True  #  All signups require an email, even for social logins
ACCOUNT_EMAIL_VERIFICATION = True  # Users must verify email addresses
SOCIALACCOUNT_AUTO_SIGNUP = False  # Don't auto-create usernames - make them pick one


# AUTOSLUG_SLUGIFY_FUNCTION = "slugify.slugify"


LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "root": {"level": "INFO"},
    "formatters": {"verbose": {"format": ("%(asctime)s %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s")}},
    "handlers": {"console": {"level": "DEBUG", "class": "logging.StreamHandler", "formatter": "verbose"}},
    "loggers": {
        # root logger
        "root": {"level": "INFO", "handlers": ["console"]},
        "django": {"level": "INFO", "handlers": ["console"]},
    },
}

# Add our apps in, allowing log = logging.getLogger(__file__) to work:
for app in LOCAL_APPS:
    LOGGING["loggers"][app.split(".")[0]] = {"level": "INFO", "handlers": ["console"]}


# We use caching on behalf of various query & view optimisations, e.g. dashboards
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "ap_cache",
        "TIMEOUT": None,
        "OPTIONS": {"MAX_ENTRIES": sys.maxsize},
    }
}
