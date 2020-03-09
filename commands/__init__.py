# -*- coding: utf-8 -*-

from app import app

def register_blueprint(app):
    # 引入 blueprint
    from commands.blueprints import bps

    for cli_group, bp_conf in bps.items():
        app.register_blueprint(bp_conf, cli_group=cli_group)


def register_commands(app):
    # 单命令直接执行
    from commands.hello import hello
    from commands.env import env
    from commands.db import db_init

    app.cli.add_command(hello)
    app.cli.add_command(env)
    app.cli.add_command(db_init)


# 加载普通命令
register_commands(app)

# 加载 blueprint 命令(cli_group 模式)
register_blueprint(app)

