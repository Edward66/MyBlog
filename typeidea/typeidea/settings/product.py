from .base import *  # NOQA

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'the1fire_db',
        'USER': 'root',
        'PASSWORD': 'Lshhxr_0310',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}



STATIC_ROOT = '/home/the1fire/venvs/typeidea-env/static_files/'

ADMINS = MANAGERS = (
    ('the1fire', '332638046@qq.com'),
)

# REDIS_URL = '127.0.0.1:6379:1'

# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': REDIS_URL,
#         'TIMEOUT': 300,
#         'OPTIONS': {
#             # 'PASSWORD': '<对应密码>',
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#             'PARSER_CLASS': 'redis.connection.HiredisParser',
#         },
#         'CONNECTION_POOL_CLASS': 'redis.connection.BlockingConnectionPool',
#     }
# }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s %(asctime)s %(module)s:'
                      '%(funcName)s:%(lineno)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'typeidea.log',
            'formatter': 'default',
            'maxBytes': 1024 * 1024,  # 1M
            'backupCount': 5,
        },

    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}
