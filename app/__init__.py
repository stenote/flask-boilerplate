from app.flask_app import create_app


class Singleton(object):
    instance = None

    def __init__(self, callback):
        self.callback = callback

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.callback(*args, **kwargs)

        return self.instance


app = Singleton(create_app)()
