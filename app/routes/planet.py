from flask import Blueprint,abort, make_response, request, Response
from app.models.planets import Planet
from app.routes.helpers import validate_planet
from ..db import db


planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    moons_n = request_body["moons_n"]

    new_planet = Planet(name=name, description=description, moons_n=moons_n)
    db.session.add(new_planet)
    db.session.commit()

    response = {
        "id": new_planet.id,
        "name": new_planet.name,
        "description": new_planet.description,
        "moons_n": new_planet.moons_n
    }
    return response, 201

@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)
    # We could also write the line above as:
    # books = db.session.execute(query).scalars()

    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "moons_n" : planet.moons_n
            }
        )
    return planets_response


# Wave_4
@planets_bp.get("/<id>")
def get_one_planet(id):
    planet = validate_planet(id)

    return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moons_n" : planet.moons_n
            }

@planets_bp.put("/<id>")
def update_planet(id):
    planet = validate_planet(id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.moons_n = request_body["moons_n"]

    db.session.commit()

    return Response(status=204, mimetype="application/json")

@planets_bp.delete("/<id>")
def delete_planet(id):
    planet = validate_planet(id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")




# # wave_1
# @planets_bp.get("/")

# def get_all_planets():
#     all_planets = []
#     for planet in planets:
#         all_planets.append(dict(
#             id = planet.id,
#             name = planet.name,
#             description = planet.description
#         ))
        
#     return all_planets


# # wave_2
# @planets_bp.get("/<id>")
# def get_one_planet(id):
#     planet = validate_planet(id)
#     return dict(
#             id = planet.id,
#             name = planet.name,
#             description = planet.description
#         )

