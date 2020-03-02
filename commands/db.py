from flask.cli import with_appcontext
from app.flask_app import app
from app.db import db

# import all  models
from app.models import *


@app.cli.command("db:init")
@with_appcontext
def db_init():
    """Database init"""
    db.create_all()
    print("Hello World!")
