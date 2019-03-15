from flask_bcrypt import Bcrypt
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'forum.login'
login_manager.login_message_category = 'info'
bcrypt = Bcrypt()