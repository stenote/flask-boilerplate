# -*- coding: utf-8 -*-
# middlewares 列表

from .test import TestMiddleware
from .foo import FooMiddleware

middlewares = [
    TestMiddleware,
    FooMiddleware,
]
