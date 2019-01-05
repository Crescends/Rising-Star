from flask import Blueprint
from flask import render_template

merch_bp = Blueprint('merch_bp', __name__, template_folder='templates', static_url_path='static')

items = {"bandana": 2.50, "hoodie": 30,  "pillow": 25,  "shirt": 5,  "sweatshirt": 15, "tank top": 10, "poster": 9.99, "album": 29.99}

@merch_bp.route('/merchandise')
def merchandise():
    return render_template('merchandise.html', title="Merchandise")

@merch_bp.route('/checkout/')
def checkout():
    return render_template('checkout.html')