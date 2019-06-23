from flask import Blueprint, render_template, flash, redirect, url_for, request, current_app
from RisingStar.forms import RegistrationForm, LoginForm, ChangePasswordForm, UpdateAccountForm, PostForm
from RisingStar.ext import bcrypt
from RisingStar.models import db, User, Post
from flask_login import login_user, current_user, logout_user, login_required
from RisingStar.routes.merchandise import fixMerch
import random
import secrets
import os

forum = Blueprint('forum', __name__, template_folder='templates', static_url_path='static/forum')

@fixMerch
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

@fixMerch
@forum.route('/forum')
def main():
    p = Post.query.all()
    return render_template('forum.html', posts=reversed(p))

@fixMerch
@forum.route('/forum/new-post', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        p = Post(title=form.subject.data, content=form.content.data, author=current_user)
        db.session.add(p)
        db.session.commit()
        flash("Your message had been created", "success")
        return redirect(url_for("forum.main"))
    return render_template('new_post.html', form=form)

@forum.route("/forum/update-post", methods=['GET', 'POST'])
@login_required
def update_post():
    post = Post.query.get_or_404(request.args.get("id"))
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.subject.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('forum.main'))
    elif request.method == 'GET':
        form.subject.data = post.title
        form.content.data = post.content
    return render_template('new_post.html', form=form)

@forum.route('/forum/delete')
@login_required
def delete_post():
    post_id = request.args.get("id")
    post = Post.query.get_or_404(post_id)
    if post.author == current_user:
        db.session.delete(post)
        db.session.commit()
        flash("Deleted Post", "info")
    else:
        flash("You are not able to delete this post", "danger")
    return redirect(url_for("forum.main"))

@fixMerch
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

    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')

@forum.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out", 'info')
    return redirect(url_for('home.home'))

def save_picture(picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(picture.filename)
    pic_filename = random_hex + f_ext 
    p_path = os.path.join(current_app.root_path, 'static', 'images', 'profile_pics',pic_filename)
    picture.save(p_path)
    return pic_filename

@fixMerch
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
        print('valid')
        if update_acct.picture.data:
            image_file = save_picture(update_acct.picture.data)
            current_user.image_file = image_file

        current_user.username = update_acct.username.data
        flash('Your username has been updated!', 'success')
        db.session.commit()
    if request.method == 'GET':
        update_acct.username.data = current_user.username
    img_src = url_for("static", filename=f'images/profile_pics/{current_user.image_file}')
    return render_template('account.html', title="Account", pssd=pass_form, update=update_acct, pfp=img_src)
