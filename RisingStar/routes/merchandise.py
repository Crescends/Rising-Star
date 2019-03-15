from flask import Blueprint, url_for, redirect
from flask import render_template, request, flash, redirect
from RisingStar.models import Merchandise, db
from flask_login import current_user, login_required

merch_bp = Blueprint('merch', __name__, template_folder='templates', static_url_path='static')

@merch_bp.route('/merchandise')
def merchandise():
    return render_template("merchandise.html", merch=Merchandise.query.all())

@merch_bp.route('/merchandise/checkout/<item>')
@login_required
def checkout(item):
    item = Merchandise.query.filter_by(name=item.replace("-", " ")).first()
    return render_template('checkout.html', title=f"Checkout {item.name}" ,item=item)

@merch_bp.route('/merchandise/shopping-cart')
@login_required
def shopping_cart():
    return render_template('shopping_cart.html', title="Purchase")

@merch_bp.route('/merchandise/add')
def add_to_cart():
    merch_id = request.args.get('id', type=int)
    if merch_id is None:
        flash("An error has occured please try again", "danger")
    else:
        order = Merchandise.query.get(merch_id)
        current_user.orders.append(order)
        db.session.commit()
        flash("The stuff has been added", "success")
    return redirect(url_for("merch.merchandise"))
