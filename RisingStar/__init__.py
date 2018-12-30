from flask import Flask
from flask import render_template

app = Flask(__name__)

def create_app():
    from . import routes
    app = Flask(__name__)
    routes.init_app(app)
    return app