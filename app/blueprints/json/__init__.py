from flask import Blueprint

json_bp = Blueprint('json', __name__)


@json_bp.route('/')
def log_index():
    return {
        'content': 'json blueprint response data'
    }
