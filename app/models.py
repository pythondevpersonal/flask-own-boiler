from app import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db

class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(200),nullable=True)
    completed = db.Column(db.Integer,default=0)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id