from .base import db
from RisingStar.ext import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    orders = db.relationship('Order', lazy=True, backref="customer") # index 0 is always the shopping cart

    @property
    def shopping_cart(self):
        return self.orders[0] if self.orders else None

    def __repr__(self):
        return f"<User> {self.username}, {self.email}"
