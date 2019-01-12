from .base import db


class Merchandise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.Integer, nullable=False) # the display name
    cost = db.Column(db.Float, nullable=False, default=0)
    image_name = db.Column(db.String(25), nullable=False)

def add_merch(db):
    db.session.add(Merchandise(type="hoodie", name="Black Campfire Jacket", cost=30.00, image_name="hoodie1.jpeg"))
    db.session.add(Merchandise(type="bandana", name="Black Campfire Jacket", cost=2.50, image_name="bandana1.jpg"))
    db.session.add(Merchandise(type=""))
    