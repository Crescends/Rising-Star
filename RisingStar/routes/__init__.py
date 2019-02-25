from flask import Flask

def init_app(app: Flask):
    from .home import home_bp
    from .merchandise import merch_bp
    from .forum import forum
    app.register_blueprint(home_bp)
    app.register_blueprint(merch_bp)
    app.register_blueprint(forum)
    app.config['SECRET_KEY'] = "2a23d85b338927f6ed0dd1d5c0ed3c83"
