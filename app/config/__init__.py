import os

env_mode = os.getenv('FLASK_ENV', 'development')

if env_mode == 'development':
    from .dev import DevConfig as Config
elif env_mode == 'production':
    from .prod import ProdConfig as Config
elif env_mode == 'testing':
    from .test import TestConfig as Config
