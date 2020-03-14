# -*- coding: utf-8 -*-

from flask import Blueprint, current_app

bp = Blueprint(__name__, __name__)


@bp.cli.command('hello')
def hello():
    """
    Demo Hello
    """
    current_app.logger.debug('Demo hello debug')
    current_app.logger.warning('Demo hello warning')
    current_app.logger.error('Demo hello error')
    current_app.logger.critical('Demo hello critical')

    print('Demo Hello')
