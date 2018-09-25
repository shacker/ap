from .common import *  # noqa: F403
import logging

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ap',
        'USER': 'you',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
    },
}

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # noqa: F405

SECRET_KEY = 'changme'

EMAIL_PORT = 1025
EMAIL_HOST = 'localhost'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]

TEST_RUNNER = 'django.test.runner.DiscoverRunner'
