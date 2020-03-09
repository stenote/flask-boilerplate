# -*- coding: utf-8 -*-
# middlewares 列表

from app.middlewares.test import TestMiddleware
from app.middlewares.foo import FooMiddleware

middlewares = [
    TestMiddleware,
    FooMiddleware,
]
