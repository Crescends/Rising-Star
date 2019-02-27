from flask import Blueprint
from flask import render_template
from RisingStar.models import Merchandise

merch_bp = Blueprint('merch_bp', __name__, template_folder='templates', static_url_path='static')

@merch_bp.route('/merchandise')
def merchandise():
    return render_template('merchandise.html', merch=Merchandise.query.all())

@merch_bp.route('/merchandise/checkout/<item>')
def checkout(item):
    item = Merchandise.query.filter_by(name=item.replace("-", " ")).first()
    return render_template('checkout.html', title=f"Checkout {item.name}" ,item=item)
