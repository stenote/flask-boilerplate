from flask import jsonify

from .base import BaseMiddleware


class JsonMiddleware(BaseMiddleware):

    def after_request(self, response):
        # 对返回结果强制进行转为 json 结果
        data = response.get_json(force=True)
        if not isinstance(data, (dict,)) or 'data' not in data:
            return jsonify({
                'code': 0,
                'data': data
            })

        # data 存在，则不进行处理
        return response
