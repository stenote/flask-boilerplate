import json

from .base import BaseMiddleware


class JsonMiddleware(BaseMiddleware):

    def after_request(self, response):
        # 进行 jsonify 返回结果进行统一处理
        if response.content_type == 'application/json':
            response.set_data(json.dumps({
                'code': 0,
                'data': response.get_json(force=True)
            }))
        return response
