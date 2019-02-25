from flask import Flask
from .base import db
from .users import User
from .posts import Post
from .merch import Merchandise, add_merch, merch_exists, merch_has_values

def init_app(app: Flask):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    db.init_app(app)
    db.app = app
    engine = db.get_engine()

    if merch_exists(engine):
        print("The merchandise table exists. Clearing table to enusure no duplicates")
        Merchandise.__table__.drop(engine)
        db.session.commit()
    Merchandise.__table__.create(engine)
    db.session.commit()
    add_merch()

__all__ = ["db", "User", "Post", "Merchandise"]
