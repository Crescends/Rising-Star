from flask import Flask
from .base import db
from .users import User
from .posts import Post
from .merch import Merchandise, add_merch, merch_exists

def init_app(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    db.init_app(app)
    db.app = app
    if merch_exists():
        Merchandise.__table__.drop(db.get_engine())
    db.create_all() 
    db.session.commit()
    add_merch()

__all__ = ["db", "User", "Post", "Merchandise"]
