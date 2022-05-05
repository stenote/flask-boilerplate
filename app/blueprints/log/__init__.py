from flask import Blueprint, current_app

log_bp = Blueprint('log', __name__)


@log_bp.route('/')
def log_index():
    current_app.logger.warn('warn log')
    current_app.logger.info('info log')
    current_app.logger.debug('debug log')
    current_app.logger.error('error log')
    current_app.logger.exception('exception log')
    current_app.logger.critical('critical info')

    return 'Log Saved !'
