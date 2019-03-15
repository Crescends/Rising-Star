from flask import Flask
from flask import render_template
from RisingStar.ext import bcrypt, login_manager
app = Flask(__name__)

def create_website():
    from RisingStar import routes, models
    app = Flask(__name__)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    routes.init_app(app)
    models.init_app(app)
    return app