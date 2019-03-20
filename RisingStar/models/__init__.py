from flask import Flask
from .base import db
from .users import User
from .posts import Post
from .merch import Merchandise, add_merch, merch_exists, merch_has_values

def init_app(app: Flask):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://LVkIsa44od:08SyDIvbeW@remotemysql.com/LVkIsa44od'
    db.init_app(app)
    db.app = app

        
__all__ = ["db", "User", "Post", "Merchandise"]
