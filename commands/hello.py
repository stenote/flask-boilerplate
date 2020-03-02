#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click

from flask.cli import with_appcontext
from app.flask_app import create_app

app = create_app()


@app.cli.command("hello")
def hello():
    """hello world."""
    print("Hello World!")
