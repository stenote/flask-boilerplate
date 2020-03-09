# -*- coding: utf-8 -*-

import traceback


from flask import abort, jsonify
from app.middlewares.base import BaseMiddleware


class TestMiddleware(BaseMiddleware):

    def before_request(self):
        print('test middleware before request')

    def after_request(self, response):
        print('test middleware after request')
        return response

    def error_handler(self, exception):
        return jsonify({
            'code': exception.code,
            'message': exception.description if hasattr(exception, 'description') else exception.message,
            'trace': traceback.format_exc().splitlines(),
        })
