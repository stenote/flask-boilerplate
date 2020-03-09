# -*- coding: utf-8 -*-

from flask import Blueprint

bp = Blueprint(__name__, __name__)


@bp.cli.command('hello')
def hello():
    """
    Demo Hello
    """
    print('Demo Hello')
