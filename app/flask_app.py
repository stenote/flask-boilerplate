#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask


def create_app():
    app = Flask(__name__.split('.')[0])
    register_config(app)

    register_blueprint(app)
    register_api(app)
    register_middleware(app)

    return app


# 注册 middlewares
def register_middleware(app):
    from app.middlewares import middlewares

    for middleware in [middleware(app) for middleware in middlewares]:
        app.before_request(middleware.before_request)
        app.after_request(middleware.after_request)

        if hasattr(middleware, 'error_handler'):
            app.errorhandler(Exception)(middleware.error_handler)


# 注册 blueprint
def register_blueprint(app):
    from app.blueprints import bps

    for url_prefix, bp in bps.items():
        app.register_blueprint(bp, url_prefix=url_prefix)


def register_api(app):
    from app.apis import apis
    for url_prefix, api in apis.items():
        app.register_blueprint(api, url_prefix='/api' + url_prefix)


# 注册配置信息
def register_config(app):
    app.config.from_pyfile('config.py')

