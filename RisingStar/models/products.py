from .base import db
import locale

locale.setlocale(locale.LC_ALL, '')
class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), unique=False, nullable=False)
    name = db.Column(db.String(50), nullable=False) # the display name
    cost = db.Column(db.String(20), nullable=False, default=0)
    image_name = db.Column(db.String(25), nullable=False)
    requests = db.relationship('Merchandise', backref='product')
    album = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return f"{self.type}: {self.name} costs {self.cost}"

def products_has_values():
    return Product.query.first() is not None

def products_exists(engine):
    return engine.dialect.has_table(engine, "product")
"""
    Not yet added
    album = Merchandise(type="album", name="Black Campfire Album", cost=25, image_name="album1.jpeg")
"""
