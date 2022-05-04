class BaseMiddleware(object):
    """
    基础 middleware
    """

    def __init__(self, app, *args, **kwargs):
        self.app = app

    def before_request(self):
        pass

    def after_request(self, response):
        return response
