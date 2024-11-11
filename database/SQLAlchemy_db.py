'''
This module make

Athor: Fetkulin Grigory, Fetkulin.G.R@yandex.ru
Starting 11/11/2024
Ending //'''
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """User model for storing user details."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)


# Configuration settings
def init_app(app):
    """AI is creating summary for init_app

    Args:
        app ([type]): [description]
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SECRET_KEY'] = 'secret_key'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
