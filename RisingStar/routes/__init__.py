from flask import Flask

def init_app(app: Flask):
    from .home import home_bp
    from .merchandise import merch_bp
    app.register_blueprint(home_bp)
    app.register_blueprint(merch_bp)
