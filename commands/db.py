from app.db import db
from app import app

# import all  models
from app.models import *


@app.cli.command('db:init')
def db_init():
    with app.app_context():
        db.create_all()
    print('Hello World!')

