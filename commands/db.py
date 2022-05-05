from app import app
from app.db import db

# import all  models
from app.models import *


@app.cli.command('db:init')
def db_init():
    db.create_all()
    print('Hello World!')
