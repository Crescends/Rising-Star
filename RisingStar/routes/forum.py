from flask import Blueprint, render_template, flash, redirect, url_for
from RisingStar.forms import RegistrationForm, LoginForm

forum = Blueprint('forum', __name__, template_folder='templates', static_url_path='static')


@forum.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}! Enjoy your time in the forum", category="success")
        redirect(url_for("forum.login"))
    return render_template('register.html', title="Register", form=form)


@forum.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)
