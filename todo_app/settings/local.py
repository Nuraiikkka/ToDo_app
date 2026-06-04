from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ro%_na^ec$9)f$7fw14tuo5fxdgryfmsf!0q_bue)3q1%3q3yy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'todo_db',
        'USER': 'todo_user',
        'PASSWORD': 'todo_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

