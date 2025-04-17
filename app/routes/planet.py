# import flask
from flask import Blueprint
from app.models.planets import planets

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

# wave_1
@planets_bp.get("/")

def get_all_planets():
    all_planets = []
    for planet in planets:
        all_planets.append(dict(
            id = planet.id,
            name = planet.name,
            description = planet.description
        ))
        
    return all_planets