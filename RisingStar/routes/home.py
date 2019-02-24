from flask import Blueprint, render_template

home_bp = Blueprint('home_bp', __name__, template_folder='templates', static_url_path='static')

@home_bp.route('/')
@home_bp.route('/home')
def home():
    return render_template('home.html', title="Home")

@home_bp.route('/about')
def about():
    return render_template('about.html', title="About")

@home_bp.route('/music')
def music():
    covers = ["Abstract", "Growth", "Smoke"]
    return render_template('music.html', covers=covers, title="Music")