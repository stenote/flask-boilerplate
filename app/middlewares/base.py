class BaseMiddleware(object):
    """
    基础 middleware
    """

    def before_request(self):
        pass

    def after_request(self, response):
        return response
