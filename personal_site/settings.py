"""
Django settings for personal_site project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_ROOT = os.path.abspath(PROJECT_PATH)
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qj@qv!#0n8vdncfg4ec(dik%)hiao&rada&716ja1(r_fu@h+g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_CONTEXT_PROCESSORS = ["django.contrib.auth.context_processors.auth",
"django.template.context_processors.debug",
"django.template.context_processors.i18n",
"django.template.context_processors.media",
"django.template.context_processors.static",
"django.template.context_processors.tz",
"django.contrib.messages.context_processors.messages",
"personal_site.context_processors.items_processor"]

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'homepage',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'personal_site.urls'

WSGI_APPLICATION = 'personal_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'personal_site',
        'USER': 'ali',
        'PASSWORD': 'password26'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = 'os.path.join(BASE_DIR, "staticfiles"),'
# STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static', 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]
