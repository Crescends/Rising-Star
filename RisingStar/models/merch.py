from .base import db

class Merchandise(db.model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), unique=True, nulable=False)
    name = db.Column(db.Integer, nulable=False) # the display name
    cost = db.Column(db.Float, nulable=False, default=0)
    image_name = db.Column(db.String(25), nulable=False)

def add_merch(db):
    db.session.add(Merchandise(type="hoodie", name="Black Campfire Jacket", cost=30.00, image_name="hoodie1.jpeg"))
    db.session.add(Merchandise(type="bandana", name="Black Campfire Jacket", cost=2.50, image_name="bandana1.jpg"))
    db.session.add(Merchandise(type=""))

sweatshirts $25, pillows are $5, shirts are $15, tank top is $10. Posters are $9.99 and albums are $29.99
