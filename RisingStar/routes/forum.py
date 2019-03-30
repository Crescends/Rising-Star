from flask import Blueprint, render_template, flash, redirect, url_for, request
from RisingStar.forms import RegistrationForm, LoginForm, ChangePasswordForm, UpdateAccountForm
from RisingStar.ext import bcrypt
from RisingStar.models import db, User, Post
from flask_login import login_user, current_user, logout_user, login_required
import random

forum = Blueprint('forum', __name__, template_folder='templates', static_url_path='static/forum')

@forum.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('forum.main'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        default_images = [f"default{i}.jpg" for i in range(1, 5)]
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, image_file=random.choice(default_images))
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created you are now able to login', 'success')
        redirect(url_for("forum.login"))
    return render_template('register.html', title="Register", form=form)

@forum.route('/forum')
def main():
    return render_template('forum.html', posts=Post.query.all())

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


@forum.route('/account', methods=["POST", "GET"])
@login_required
def account():
    pass_form = ChangePasswordForm()
    update_acct = UpdateAccountForm()
    if pass_form.submit.data and pass_form.validate_on_submit():
        if bcrypt.check_password_hash(current_user.password, pass_form.old_password.data):
            current_user.password = bcrypt.generate_password_hash(pass_form.new_password.data).decode("utf-8")
            flash("Your password has been updated!!!", "success")
        else:
            flash("The Password is not correct", "danger")
        db.session.commit()

    if update_acct.submit2.data and update_acct.validate_on_submit():
        print('data')
        current_user.username = update_acct.username.data
        print(current_user.username)
        flash('Your username has been updated!', 'success')
        db.session.commit()
    img_src = url_for("static", filename=f'images/profile_pics/{current_user.image_file}')
    return render_template('account.html', title="Account", pssd=pass_form, update=update_acct, pfp=img_src)