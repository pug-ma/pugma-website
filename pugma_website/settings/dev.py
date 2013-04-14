from .base import *


# Debug
DEBUG = True
TEMPLATE_DEBUG = True

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': path('database.db'),
    }
}