import os
import logging


def o(key, default=None):
    """
    通过环境变量快速获取配置信息的函数
    @param key:
    @param default:
    @return:
    """
    return os.getenv(key, default)


class BaseConfig(object):
    APP_NAME = o('APP_NAME', 'flask')

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
