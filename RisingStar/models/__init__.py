from flask import Flask
from .base import db
from .users import User
from .order import Order
from .posts import Post
from .merch import Merchandise
from .products import Product, add_products, products_exists, products_has_values

def init_app(app: Flask):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://LVkIsa44od:08SyDIvbeW@remotemysql.com/LVkIsa44od'
    db.init_app(app)
    db.app = app

__all__ = ["db", "User", "Post", "Merchandise", "Order", "Product"]
