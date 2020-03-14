# -*- coding: utf-8 -*-

import logging

# Database
SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/may/Code/marui/test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True


LOGGING = [
    {
        'level': logging.WARNING,
        'handler': logging.FileHandler.__name__,
        'handler_args': [
            'flask.log'
        ],
        'format': '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s',
    },
]

REMOVE_DEFAULT_LOGGING = True
