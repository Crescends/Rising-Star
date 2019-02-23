from flask import Flask
from flask import render_template

app = Flask(__name__)

def create_website():
    from . import routes, models
    app = Flask(__name__)
    routes.init_app(app)
    models.init_app(app)
    return app