import os

env_mode = os.getenv('FLASK_ENVIRONMENT', 'dev')

if env_mode == 'dev':
    from .dev import DevConfig as Config
elif env_mode == 'prod':
    from .prod import ProdConfig as Config
elif env_mode == 'test':
    from .test import TestConfig as Config
