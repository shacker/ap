'''
Test settings

- Used to run tests fast on the continuous integration server and locally
'''
from .common import *  # noqa


# DEBUG
# ------------------------------------------------------------------------------
# Turn debug off so tests run faster
DEBUG = False
TEMPLATES[0]['OPTIONS']['debug'] = False  # noqa: F405

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = 'CHANGEME!!!'

# Mail settings
# ------------------------------------------------------------------------------
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

# In-memory email backend stores messages in django.core.mail.outbox
# for unit testing purposes
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# CACHING
# ------------------------------------------------------------------------------
# Speed advantages of in-memory caching without having to run Memcached
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
    }
}

# File Storage
# ------------------------------------------------------------------------------
# Instead of having to deal with S3/boto for dynamically spun up test envs, use local file store
# (PB: but isn't this the default already? setting explicitly just-in-case...)
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'


# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'


# PASSWORD HASHING
# ------------------------------------------------------------------------------
# Use fast password hasher so tests run faster
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# TEMPLATE LOADERS
# ------------------------------------------------------------------------------
# Keep templates in memory so tests run faster
TEMPLATES[0]['OPTIONS']['loaders'] = [  # noqa: F405
    ['django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ], ],
]

# Higher level of logging in local development environments.

for app in LOCAL_APPS:  # noqa: F405
    LOGGING['loggers'][app.split('.')[0]] = {  # noqa: F405
        'level': 'DEBUG',
        # 'level': 'WARNING',  # Uncomment if test runner is showing too much output
        'handlers': ['console'],
    }
