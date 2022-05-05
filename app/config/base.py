import os
import logging


class BaseConfig(object):
    APP_NAME = os.getenv('APP_NAME', 'flask')

    # Database
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    LOGGING = [
        {
            'level': logging.INFO,
            'handler': logging.FileHandler.__name__,
            'handler_args': [
                '{}.log'.format(APP_NAME),
            ],
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
        }
    ]
