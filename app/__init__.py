from flask import Flask
from .db import db, migrate
from .models import planets, moon
from .routes.planet import bp as planets_bp
from flask_sqlalchemy import SQLAlchemy
from .routes.moon_routes import bp as moon_bp
import os

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    if test_config:
        # Merge `config` into the app's configuration
        # to override the app's default settings
        app.config.update(test_config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    app.register_blueprint(planets_bp)
    app.register_blueprint(moon_bp)

    return app