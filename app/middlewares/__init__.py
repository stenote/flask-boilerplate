# middlewares 列表
from .demo import DemoMiddleware
from .json import JsonMiddleware

# common_middlewares 为通用 middleware, 所有请求都来使用
# 其他 middleware 由 blueprint 来决定是否使用
common_middlewares = [
    DemoMiddleware,
]
