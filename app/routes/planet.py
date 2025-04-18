from flask import Blueprint
from app.models.planets import planets
from app.routes.helpers import validate_planet


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


# wave_2
@planets_bp.get("/<id>")
def get_one_planet(id):
    planet = validate_planet(id)
    return dict(
            id = planet.id,
            name = planet.name,
            description = planet.description
        )

