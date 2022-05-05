import traceback
from flask import jsonify

from .base import BaseMiddleware


class DemoMiddleware(BaseMiddleware):

    def before_request(self):
        print('demo middleware before request')

    def after_request(self, response):
        print('demo middleware after request')
        return response

    def error_handler(self, exception):
        return jsonify({
            'code': exception.code,
            'message': exception.description if hasattr(exception, 'description') else exception.message,
            'trace': traceback.format_exc().splitlines(),
        })
