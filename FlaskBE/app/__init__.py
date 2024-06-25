from flask import Flask
from .extensions import db
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    from .blueprints import register_blueprints
    register_blueprints(app)

    return app
