import os
import sys

from os.path import dirname
from os.path import abspath


# Project Information
PROJECT_ROOT = dirname(dirname(dirname(abspath(__file__))))
PROJECT_NAME = os.path.basename(PROJECT_ROOT)

# Helpers
path = lambda *args: os.path.join(PROJECT_ROOT, *args)

# Debug
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Manager
ADMINS = (
    ('hersonls', 'hersonls@gmail.com'),
    ('raelmax', 'contato@raelmax.com'),
    ('helton', 'helton99@hotmail.com'),
)
MANAGERS = ADMINS

# Database
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE', ''),
        'NAME': os.environ.get('DATABASE_NAME', ''),
        'USER': os.environ.get('DATABASE_USER', ''),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
        'HOST': os.environ.get('DATABASE_HOST', ''),
        'PORT': os.environ.get('DATABASE_PORT', ''),
    }
}

# Site
ALLOWED_HOSTS = []
SITE_ID = 1
SECRET_KEY = 'v1$+lvszttsiowgzn$6uk!$ux3d^ed@c34#l^0c9kl+6pu=9wz'
WSGI_APPLICATION = 'pugma_website.wsgi.application'

# Urls
ROOT_URLCONF = 'pugma_website.urls'

# Internationalization
TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Media and Static
MEDIA_ROOT = path('media')
MEDIA_URL = '/m/'
STATIC_ROOT = path('static')
STATIC_URL = '/s/'

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# Template
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'apps.page.context_processors.projects',
    'apps.page.context_processors.next_event',
)

# Middleware 
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Templates
TEMPLATE_DIRS = (path('templates'), )

# Apps
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    # Project Apps
    'apps.page',
    'apps.blog',
    'apps.projects',
    
    # Third-party Apps
    'tagging',
    'redactor',
    'south'
)

# Log
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# WYSIWYG Redactor
REDACTOR_OPTIONS = {'lang': 'pt_br'}
REDACTOR_UPLOAD = '%scontent-uploads/'.format(MEDIA_URL)
