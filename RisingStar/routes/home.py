from flask import Blueprint, render_template

home_bp = Blueprint('home_bp', __name__, template_folder='templates', static_url_path='static')

@home_bp.route('/')
@home_bp.route('/home')
def home():
    return render_template('home.html', title="Home")

@home_bp.route('/merchandise')
def merchandise():
    return render_template('merchandise.html', title="Merchandise")