from flask import Blueprint,abort, make_response, request, Response
from app.models.planets import Planet
from app.routes.helpers import validate_model
from ..db import db


planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    response = new_planet.to_dict()
    return response, 201

@planets_bp.get("")
def get_all_planets():

    # query = db.select(Planet).order_by(Planet.id)
    query = db.select(Planet)
    
    name_param = request.args.get("name")
    if name_param:
        query = query.where(Planet.name.ilike(f"%{name_param}%"))

    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))

    planets = db.session.scalars(query.order_by(Planet.id))

    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_dict())
    return planets_response


# Wave_4
@planets_bp.get("/<id>")
def get_one_planet(id):
    planet = validate_model(Planet, id)

    return planet.to_dict()

@planets_bp.put("/<id>")
def update_planet(id):
    planet = validate_model(Planet, id)
    request_body = request.get_json()

    # planet.name = request_body["name"]
    # planet.description = request_body["description"]
    # planet.moons_n = request_body["moons_n"]

    # Three lines above can be replaced with a instance method
    planet.update_from_dict(request_body)

    db.session.commit()

    return Response(status=204, mimetype="application/json")

@planets_bp.delete("/<id>")
def delete_planet(id):
    planet = validate_model(Planet, id)
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

