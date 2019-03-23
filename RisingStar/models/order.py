from .base import db

purchases = db.Table('purchases',
    db.Column("merch_id", db.Integer, db.ForeignKey('merchandise.id'), primary_key=True),
    db.Column("order_id", db.Integer, db.ForeignKey('order.id'), primary_key=True))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer , db.ForeignKey('user.id'))
    merch = db.relationship('Merchandise', lazy=True, secondary=purchases, backref="requests")
