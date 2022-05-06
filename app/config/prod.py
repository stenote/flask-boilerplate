from redis import Redis

from .base import BaseConfig


class ProdConfig(BaseConfig):
    SESSION_TYPE = 'redis'
    SESSION_REDIS = Redis(
        host='127.0.0.1',
        port=6379
    )

    # 强制加 salt
    SESSION_USE_SIGNER = True
    SECRET_KEY = 'wVdq^Fia$Az6m$oB%97$cXhqjDxNc9vZ'  # 自行生成即可

    # 长期有效
    SESSION_PERMANENT = True
    PERMANENT_SESSION_LIFETIME = 3600  # 1h
