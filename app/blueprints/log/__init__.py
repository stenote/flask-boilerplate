from flask import Blueprint, current_app

log_bp = Blueprint('log', __name__)


@log_bp.route('/')
def log_index():
    current_app.logger.warn('hello world')
    current_app.logger.debug('debug info')
    return 'logging'
