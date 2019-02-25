from .base import db
import locale

locale.setlocale(locale.LC_ALL, '')
class Merchandise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), unique=False, nullable=False)
    name = db.Column(db.Integer, nullable=True) # the display name
    cost = db.Column(db.String, nullable=False, default=0)
    image_name = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return f"{self.type}: {self.name} costs {self.cost}"

hoodie = Merchandise(type="hoodie", name="Black Campfire Jacket", cost=locale.currency(30.00), image_name="hoodie1.jpg")
bandana = Merchandise(type="bandana", name="Black Campfire Bandana", cost=locale.currency(2.50), image_name="bandana1.jpeg")
pillow = Merchandise(type="pillow", name="Black Campfire Pillow", cost=locale.currency(25), image_name="pillow1.jpeg")
shirt = Merchandise(type="shirt", name="Black Campfire Shirt", cost=locale.currency(25), image_name="shirt1.jpeg")
sweat_shirt = Merchandise(type="sweat_shirt", name="Black Campfire Sweat Shirt", cost=locale.currency(25), image_name="sweat_shirt1.jpeg")
sweat_shirt2 = Merchandise(type="sweat_shirt", name="Abstract Campfire Sweat Shirt", cost=locale.currency(25), image_name="sweat_shirt2.jpeg")
tank = Merchandise(type="tank", name="Black Campfire Tank Top", cost=locale.currency(25), image_name="tank1.jpeg")
poster = Merchandise(type="poster", name="Campfire Poster", cost=locale.currency(10), image_name="artist1.png")
pants = Merchandise(type="pants", name="White Abstract Pants", cost=locale.currency(25), image_name="sweatpants1.jpg")

merch = [hoodie, bandana, pillow, shirt, sweat_shirt, sweat_shirt2, tank, poster, pants]
def add_merch():
    for item in merch:
        db.session.add(item)
    db.session.commit()

def merch_exists():
    return Merchandise.query.first() is not None # Check if empty
"""
    Not yet added
    album = Merchandise(type="album", name="Black Campfire Album", cost=25, image_name="album1.jpeg")
"""
