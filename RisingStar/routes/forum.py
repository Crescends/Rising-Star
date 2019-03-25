from flask import Blueprint, render_template, flash, redirect, url_for, request
from RisingStar.forms import RegistrationForm, LoginForm
from RisingStar.ext import bcrypt
from RisingStar.models import db, User
from flask_login import login_user, current_user, logout_user, login_required

forum = Blueprint('forum', __name__, template_folder='templates', static_url_path='static/forum')


@forum.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('forum.main'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created you are now able to login', 'success')
        redirect(url_for("forum.login"))
    return render_template('register.html', title="Register", form=form)

@forum.route('/forum')
def main():
    return render_template('forum.html')

@forum.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('forum.main'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash("You are now logged in", "success")
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for("home.home"))
        else:
            flash("The Username or password is incorrect", "danger")
    return render_template('login.html', title="Login", form=form)

@forum.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out", 'info')
    return redirect(url_for('home.home'))


@forum.route('/account')
@login_required
def account():
    return render_template('account.html', title="Account")