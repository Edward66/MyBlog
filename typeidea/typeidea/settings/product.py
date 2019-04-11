from .base import *  # NOQA

DEBUG = False

ALLOWED_HOSTS = ['the1fire.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'the1fire_db',
        'USER': 'root',
        'PASSWORD': '112233',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

REDIS_URL = '127.0.0.1:6379:1'

CACHE = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'lOCATION': 'REDIS_URL',
        'TIMEOUT': 300,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
        'CONNECTION_POOL_CLASS': 'redis.connection.BlockingConnectionPool',
    }
}
