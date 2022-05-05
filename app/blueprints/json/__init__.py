from flask import Blueprint

from app.decorator import common_response
from app.middlewares import json

json_bp = Blueprint('json', __name__)

# json_bp 需要对所有结果都处理为 json 数据
"""
{
    "code": 0,
    "data": {
        "key": "value"
    }
}
"""

json_bp.after_request(json.JsonMiddleware().after_request)


@json_bp.route('/')
@common_response
def log_index():
    """
    手动处理返回可被处理为 response 的数据结构
    @return:
    """
    return 0
