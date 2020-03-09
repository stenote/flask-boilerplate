# -*- coding: utf-8 -*-

from app.middlewares.base import BaseMiddleware


class FooMiddleware(BaseMiddleware):

    def before_request(self):
        print('foo before request')

    def after_request(self, response):
        print('foo after request')
        return response
