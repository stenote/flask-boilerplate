# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

demo_bp = Blueprint(__name__, __name__)


@demo_bp.route('/')
@demo_bp.route('/hello/')
@demo_bp.route('/hello/<names>')
def demo_index(names=None):
    if names is None:
        names = [
            'Li'
        ]
    else:
        names = names.split(',')

    return render_template('demo/index.html', names=names)
