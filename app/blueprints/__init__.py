from .demo import demo_bp
from .log import log_bp
from .json import json_bp

bps = {
    '/demo': demo_bp,
    '/log': log_bp,
    '/json': json_bp,
}
