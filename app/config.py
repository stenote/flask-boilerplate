import logging

APP_NAME = 'flask'

# Database
SQLALCHEMY_DATABASE_URI = ''
SQLALCHEMY_TRACK_MODIFICATIONS = True


LOGGING = [
    {
        'level': logging.DEBUG,
        'handler': logging.FileHandler.__name__,
        'handler_args': [
            '{}.log'.format(APP_NAME),
        ],
        'format': '[%(asctime)s] %(levelname)s %(filename)s %(funcName)s [%(lineno)s]: %(message)s',
    },
    {
        'level': logging.INFO,
        'handler': logging.StreamHandler.__name__,
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    }
]
