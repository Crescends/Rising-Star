from .base import db

purchases = db.Table('purchases',
          db.Column("user_id", db.Integer, db.ForeignKey('user.id'), primary_key=True)
          db.Column("merch_id", db.Integer, db.ForeignKey('merchandise.id'), primary_key=True)
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    full_name = db.Column(db.String(100), unique = false, nullable=false)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    orders = db.relationship('Merchandise', lazy=True)

    def __repr__(self):
        return f"<User> {self.username}, {self.email}"
