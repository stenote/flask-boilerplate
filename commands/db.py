import click
from app.db import db

# import all  models
from app.models import *


@click.command('db:init')
def db_init():
    """Database init"""
    db.create_all()
    print("Hello World!")
