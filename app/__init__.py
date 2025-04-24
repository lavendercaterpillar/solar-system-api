from flask import Flask
from .db import db, migrate
from .models import planets
from .routes.planet import planets_bp

def create_app():
    app = Flask(__name__)
    db_name = 'solar_system_development'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://postgres:postgres@localhost:5432/{db_name}'

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    app.register_blueprint(planets_bp)

    return app
