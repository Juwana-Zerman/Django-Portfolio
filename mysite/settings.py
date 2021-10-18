import os
from pathlib import Path
import django_heroku
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
"""
Try this site: https://stackoverflow.com/questions/66593382/how-to-pass-secrets-from-github-actions-to-python-environ-variables
"""
# Add a comma after SECRET_KEY here and enter your generated key between quotes ('SECRET_KEY', '') see below to generate
SECRET_KEY = os.environ.get('SECRET_KEY')
# Remove SECRET_KEY before pushing to GitHub

# To generate a secret key run the following command in the terminal:
# python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # switch to True to run locally

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'https://zerman-portfolio.herokuapp.com/']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'mysite',
    'home',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

Template_Dir = Path(BASE_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [Template_Dir],
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

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


# Comment out this DATABASES section to run the project on your local machine
# Uncomment the sqlite3 section to run on you local machine

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'djangoportfolio',
#         'USER': 'postgres',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# ************Uncomment this DATABASES section to run the project on your local machine*******
# ************Do not commit this settings.py file or push to GitHub**************

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'sqlite3.db',
#     }
# }


db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (str(BASE_DIR.joinpath('mysite/static/')),)
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'testemail@gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_PORT = 1025

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Activate Django-Heroku
django_heroku.settings(config=locals(), staticfiles=False)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] '
                       'pathname=%(pathname)s lineno=%(lineno)s '
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}
