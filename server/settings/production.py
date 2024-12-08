from .base import *
from dotenv import load_dotenv

load_dotenv()

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.getenv('PRODUCTION_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'koyebdb',
        'USER': 'koyeb-adm',
        'PASSWORD': 'ak4PtzswUE2L',
        'HOST': 'ep-fancy-violet-a4dom35y.us-east-1.pg.koyeb.app',
        'OPTIONS': {'sslmode': 'require'},
    }
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
