import os
from .settings import *
from .settings import BASE_DIR

SECRET_KEY = os.environ['SECRET']

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CRSF_TRUSTED_ORIGINS = ['https://'+ os.environ['WEBSITE_HOSTNAME']]

DEBUG = False
TEMPLATE_DEBUG = False


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
]
INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    "admin_interface",
    "colorfield",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "frontapp",
    "crispy_forms",
    "crispy_bootstrap5",
    "debug_toolbar",
    "admin_honeypot",
    "admin_reorder",
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_URL = os.path.join(BASE_DIR, '/myProject/staticfiles/')
STATIC_ROOT = os.path.join(BASE_DIR, '/myProject/staticfiles')

connection_string = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
parameters = {pair.split('=')[0]: pair.split('=')[1] for pair in connection_string.split(' ')}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': parameters['dbname'],
        'HOST': parameters['host'],
        'USER': parameters['user'],
        'PASSWORD': parameters['password'],
        'OPTIONS': {'sslmode': 'require'},
    }
}