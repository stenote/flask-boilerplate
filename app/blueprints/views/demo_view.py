# -*- coding: utf-8 -*-

from flask import render_template

# 导入 demo blueprint，进行 route 渲染
from ..demo import demo as demo_view


@demo_view.route('/')
@demo_view.route('/hello/')
@demo_view.route('/hello/<names>')
def demo_index(names=None):
    if names is None:
        names = [
            'Li'
        ]
    else:
        names = names.split(',')

    return render_template('demo/index.html', names=names)
