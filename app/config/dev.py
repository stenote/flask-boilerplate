import logging
from .base import BaseConfig


class DevConfig(BaseConfig):
    DEBUG = True

    # debug level 日志以文件形式存储，便于 debug, 会覆盖 flask 的 default_handler
    LOGGING = [
        {
            'level': logging.DEBUG,
            'handler': logging.FileHandler.__name__,
            'handler_args': [
                '{}_dev.log'.format(BaseConfig.APP_NAME),
            ],
            'format': '[%(asctime)s] %(levelname)s %(filename)s %(funcName)s [%(lineno)s]: %(message)s',
        },
        {
            'level': logging.INFO,
            'handler': logging.StreamHandler.__name__,
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
        },
    ]
