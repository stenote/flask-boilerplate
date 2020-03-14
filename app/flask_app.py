#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from flask import Flask
from flask.logging import default_handler


def create_app():
    app = Flask(__name__.split('.')[0])
    register_config(app)
    register_logger(app)
    register_middleware(app)
    register_blueprint(app)
    register_api(app)

    return app


def register_logger(app):
    """
    注册 logger
    :param app:
    :return:  none
    """

    # remove default logging if need
    if app.config.get('REMOVE_DEFAULT_LOGGING', False):
        app.logger.removeHandler(default_handler)

    for log_conf in app.config.get('LOGGING', []):
        log_level = log_conf.get('level', logging.WARNING)

        if log_level < logging.WARNING:
            app.debug = True

        # instance handler
        handler = getattr(logging, log_conf.get('handler'))(
            *log_conf.get('handler_args'))
        handler.setLevel(log_level)

        log_format = logging.Formatter(log_conf.get('format'))
        handler.setFormatter(log_format)

        # register logger
        app.logger.addHandler(handler)


def register_middleware(app):
    """
    给 app 注册中间件
    :param app: flask instance
    :return: none
    """
    from app.middlewares import middlewares

    for middleware in [middleware(app) for middleware in middlewares]:
        app.before_request(middleware.before_request)
        app.after_request(middleware.after_request)

        if hasattr(middleware, 'error_handler'):
            app.errorhandler(Exception)(middleware.error_handler)


def register_blueprint(app):
    """
    注册 blueprint
    :param app: flask instance
    :return: none
    """
    from app.blueprints import bps

    for url_prefix, bp in bps.items():
        app.register_blueprint(bp, url_prefix=url_prefix)


def register_api(app):
    """
    注册 api namespace 下的 blueprint
    :param app: flask instance
    :return: none
    """
    from app.apis import apis
    for url_prefix, api in apis.items():
        app.register_blueprint(api, url_prefix='/api' + url_prefix)


def register_config(app):
    """
    注册配置信息
    :param app: flask instance
    :return: none
    """
    app.config.from_pyfile('config.py')
