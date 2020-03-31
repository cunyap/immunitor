"""Initialize app."""
import os
from flask import Flask
from flask_qrcode import QRcode
from flask_bootstrap import Bootstrap


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    bootstrap = Bootstrap(app)
    qrcode = QRcode(app)
    app.config.from_object('config.Config')
    app.config['SECRET_KEY'] = os.environ['APP_SECRET_KEY']
    app.config['RECAPTCHA_USE_SSL'] = False
    app.config['RECAPTCHA_PUBLIC_KEY'] = os.environ['APP_RECAPTCHA_PUBLIC_KEY']
    app.config['RECAPTCHA_PRIVATE_KEY'] = os.environ['APP_RECAPTCHA_PRIVATE_KEY']
    app.config['RECAPTCHA_OPTIONS'] = {'theme': 'white'}

    with app.app_context():
        # Import parts of our application
        from . import routes
        return app
