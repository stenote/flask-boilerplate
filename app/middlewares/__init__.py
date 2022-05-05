# middlewares 列表
from .demo import DemoMiddleware
from .json import JsonMiddleware

middlewares = [
    DemoMiddleware,
    JsonMiddleware,
]
