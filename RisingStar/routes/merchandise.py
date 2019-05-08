from flask import Blueprint, url_for, redirect
from flask import render_template, request, flash, redirect
from RisingStar.models import Merchandise, db, Order, Product
from flask_login import current_user, login_required

merch_bp = Blueprint('merch', __name__, template_folder='templates', static_url_path='static')

@merch_bp.route('/merchandise')
def merchandise():
    args = request.args
    category_field = "All Categories"
    album_field = "All types"
    try:
        chosen_products = Product.query.filter(Product.type != "Tour Ticket")
    except:
        chosen_products = Product.query.filter(Product.type != "Tour Ticket")

    t = args.get("type", None, type=str)
    if t:
        chosen_products = chosen_products.filter_by(type=t)
        category_field = t
    price = args.get("price", None)
    if price:
        chosen_products.filter_by(price=price)    
    album = args.get("album", None)
    if album:    
        print("choosing album", album)
        chosen_products = chosen_products.filter_by(album=album)
        album_field = album
    albums = ["Abstract", "Smoke", "Growth"]
    types = "Shirt", "Tank Top", "Sweatpants", "Iphone Case", "Galaxy Case", "Pillow", "Sweatshirt", "Bandana", "Poster", "Hoodie"
    return render_template('merchandise.html', albums=albums,merch=chosen_products.all(), types=types, album_field=album_field, category_field=category_field)

@merch_bp.route('/merchandise/checkout/')
@login_required
def checkout():
    item = Product.query.get_or_404(request.args.get("id"))
    return render_template('checkout.html', title=f"Checkout {item.name}" ,item=item)

@merch_bp.route('/merchandise/shopping-cart')
@login_required
def shopping_cart():
    return render_template('shopping_cart.html', title="Purchase")

@merch_bp.route('/merchandise/add')
def add_to_cart():
    if not current_user.shopping_cart:
        current_user.orders.append(Order(is_cart=True, user=current_user))
    product_id = request.args.get('id', type=int)
    if product_id is None:
        flash("An error has occured please try again", "danger")
    else: 
        product = Product.query.get(product_id)
        current_user.shopping_cart.merch.append(Merchandise(product=product))
        db.session.commit()
        flash("The stuff has been added", "success")
    return redirect(url_for("merch.merchandise"))

@merch_bp.route('/merchandise/purchase-cart')
@login_required
def checkout_cart():
    shopping_cart = current_user.shopping_cart
    new_order = Order(customer=current_user, merch=shopping_cart.merch, is_cart=False)
    shopping_cart.merch = []
    db.session.add(new_order)
    db.session.commit()
    return redirect(url_for("merch.shopping_cart"))

@merch_bp.route('/merchandise/delete')
@login_required
def delete_from_cart():
    merch_id = request.args.get("id", type=int)
    if merch_id is None:
        flash("An error has occured", "danger")
    else:
        merch_order = Merchandise.query.get_or_404(merch_id)
        db.session.delete(merch_order)
        db.session.commit()
    return redirect(url_for("merch.shopping_cart"))
