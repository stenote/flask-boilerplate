from app.db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, unique=True)
    username = db.Column(db.String(255))

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<User {username}>'.format(username=self.username)
