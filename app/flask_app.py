import logging
from flask import Flask


class App(Flask):

    def load_config(self):
        """
        载入配置信息
        :param self: flask instance
        :return self: flask instance
        """
        from .config import Config
        self.config.from_object(Config)

        return self

    def init_logger(self):
        """
        注册 logger
        :param self: flask instance
        :return self: flask instance
        """
        # logger 单例
        logger = logging.getLogger(self.name)

        for log_conf in self.config.get('LOGGING', []):
            log_level = log_conf.get('level', logging.WARNING)

            # debug 级别开启 debug
            if log_level < logging.WARNING:
                self.debug = True

            # instance handler
            handler = getattr(logging, log_conf.get('handler'))(
                *log_conf.get('handler_args', [])
            )

            handler.setLevel(log_level)

            log_format = logging.Formatter(log_conf.get('format'))
            handler.setFormatter(log_format)

            # register logger
            logger.addHandler(handler)

        return self

    def init_app(self):
        return self

    def load_common_middlewares(self):
        """
        给 app 注册中间件
        :param self: flask instance
        :return self: flask instance
        """
        from app.middlewares import common_middlewares

        for middleware in [middleware() for middleware in common_middlewares]:
            self.before_request(middleware.before_request)
            self.after_request(middleware.after_request)

            if hasattr(middleware, 'error_handler'):
                self.errorhandler(Exception)(middleware.error_handler)

        return self

    def load_blueprints(self):
        """
        注册 blueprint
        :param self: flask instance
        :return self: flask instance
        """
        from app.blueprints import bps

        for url_prefix, bp in bps.items():
            self.register_blueprint(bp, url_prefix=url_prefix)
        return self

    def load_api(self):
        """
        1. 注册 api namespace 下的 blueprint
        2. 注册 restful API
        :param self: flask instance
        :return self: flask instance
        """
        from app.apis import apis
        for url_prefix, api in apis.items():
            self.register_blueprint(api, url_prefix='/api' + url_prefix)

        return self


def create_app():
    app = App(__name__.split('.')[0])

    (
        app.load_config()
        .init_app()
        .load_common_middlewares()
        .load_blueprints()
        .load_api()
    )

    return app
