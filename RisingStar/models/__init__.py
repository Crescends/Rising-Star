from flask import Flask
from .base import db
from .users import User
from .order import Order
from .posts import Post
from .merch import Merchandise
from .products import Product

def init_app(app: Flask):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://hhdrcnez:jiFZZEILKXgkIufeTeRFudn6mFXkPGUf@salt.db.elephantsql.com:5432/hhdrcnez"
    db.init_app(app)
    db.app = app

__all__ = ["db", "User", "Post", "Merchandise", "Order", "Product"]
