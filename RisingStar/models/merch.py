from .base import db

class Merchandise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), unique=False, nullable=False)
    name = db.Column(db.Integer, nullable=True) # the display name
    cost = db.Column(db.Float, nullable=False, default=0)
    image_name = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return f"{self.type}: {self.name} costs {self.cost}"

hoodie = Merchandise(type="hoodie", name="Black Campfire Jacket", cost=30.00, image_name="hoodie1.jpeg")
bandana = Merchandise(type="bandana", name="Black Campfire Bandana", cost=2.50, image_name="bandana1.jpeg")
pillow = Merchandise(type="pillow", name="Black Campfire Pillow", cost=25, image_name="pillow1.jpeg")
shirt = Merchandise(type="shirt", name="Black Campfire Shirt", cost=25, image_name="shirt1.jpeg")
sweat_shirt = Merchandise(type="sweat_shirt", name="Black Campfire Sweat Shirt", cost=25, image_name="sweat_shirt1.jpeg")
tank = Merchandise(type="tank", name="Black Campfire Tank Top", cost=25, image_name="tank1.jpeg")

def add_merch():
    db.session.add(hoodie)
    db.session.add(bandana)
    db.session.add(pillow)
    db.session.add(shirt)
    db.session.add(sweat_shirt)
    db.session.add(tank)
    db.session.commit()
"""
    Not yet added
    poster = Merchandise(type="poster", name="Black Campfire Poster", cost=25, image_name="poster1.jpeg")
    pants = Merchandise(type="pants", name="Black Campfire Pants", cost=25, image_name="pants1.jpeg")
    album = Merchandise(type="album", name="Black Campfire Album", cost=25, image_name="album1.jpeg")
"""
