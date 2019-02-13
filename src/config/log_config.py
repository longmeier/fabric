# coding:utf-8
"""log配置经常要调整，集中到一个文件中。更清晰点"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s | %(levelname)s | %(name)s:%(lineno)s | %(funcName)s | %(process)d | %(thread)d | %(threadName)s | %(message)s'
        },
        'simple': {
            'format': ' %(asctime)s | %(levelname)s | %(name)s:%(lineno)s | %(message)s'
        },
        'rq_console': {
            'format': '%(asctime)s | %(message)s',
            'datefmt': '%H:%M:%S',
        },

    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            # 'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple',

        },
        'db_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/db.log'),
            'formatter': 'simple',
            'encoding': 'utf8',
        },
        'tools_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/tools.log'),
            'formatter': 'simple',
            'encoding': 'utf8',
        },
        'users_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/users.log'),
            'formatter': 'simple',
            'encoding': 'utf8',
        },
        'root_other': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/root.log'),
            'formatter': 'simple',
            'encoding': 'utf8',
        },
    },
    'root': {
        'handlers': ['root_other', 'console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'ERROR'
        },
        'django.db': {
            'handlers': ['db_file'],
            'level': 'DEBUG',
            'propagate': True
        },
        'tools': {
            'handlers': ['tools_file', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'users': {
            'handlers': ['users_file', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },

    },

}
