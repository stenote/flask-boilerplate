# -*- coding: utf-8 -*-

from flask import Blueprint,  jsonify

demo_api = Blueprint(__name__, __name__)


@demo_api.route('/')
def demo_index():

    return jsonify({
        'hello': 'world'
    })
