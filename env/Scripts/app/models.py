from flask_sqlalchemy import SQLAlchemy
from main import app

db = SQLAlchemy(app)

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, nullable=False)
    login = db.Column(db.String(80), unique=True, nullable=False)
    task = db.Column(db.String(200), nullable=False)
