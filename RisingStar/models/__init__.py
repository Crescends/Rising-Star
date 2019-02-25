from flask import Flask
from .base import db
from .users import User
from .posts import Post
from .merch import Merchandise, add_merch, merch_exists

def init_app(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    db.init_app(app)
    db.app = app
    db.create_all()
    if not merch_exists():
        add_merch()

__all__ = ["db", "User", "Post", "Merchandise"]
