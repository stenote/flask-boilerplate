from flask import Blueprint,  jsonify

demo_api = Blueprint('demo_api', __name__)


@demo_api.route('/')
def demo_index():

    return jsonify({
        'hello': 'world'
    })
