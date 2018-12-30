from flask import Flask

def init_app(app: Flask):
    from .home import home_bp
    app.register_blueprint(home_bp)
