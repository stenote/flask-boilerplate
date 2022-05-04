from .demo import demo_bp
from .log import log_bp

bps = {
    '/demo': demo_bp,
    '/log': log_bp
}
