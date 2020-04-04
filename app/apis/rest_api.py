# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restplus import Api, Resource, apidoc

rest_api = Blueprint(__name__, __name__)


api = Api(rest_api, doc='/doc/')


@api.documentation
def swagger_ui():
    return apidoc.ui_for(api)


@api.route('/')
class Hello(Resource):
    def get(self):
        return {
            'hello': 'world'
        }

