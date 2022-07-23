from app import db
from datetime import datetime


class Admin(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(50), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<Admin {}>'.format(self.username)
