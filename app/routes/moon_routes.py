from flask import Blueprint,abort, make_response, request, Response
from app.models.moon import Moon
from app.models.moon import Moon
from app.routes.helpers import validate_model
from ..db import db


bp = Blueprint("moon_bp", __name__, url_prefix="/moon")

@bp.post("")
def create_moon():
    request_body = request.get_json()
    
    try:
        new_moon = Moon.from_dict(request_body)

    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))
        
    db.session.add(new_moon)
    db.session.commit()

    response = new_moon.to_dict()
    return response, 201


@bp.get("")
def get_all_moons():

    # query = db.select(Moon).order_by(Moon.id)
    query = db.select(Moon)
    
    size_param = request.args.get("name")
    if size_param:
        query = query.where(Moon.name.ilike(f"%{size_param}%"))

    description_param = request.args.get("description")
    if description_param:
        query = query.where(Moon.description.ilike(f"%{description_param}%"))

    moons = db.session.scalars(query.order_by(Moon.id))

    moon_response = []
    for moon in moons:
        moon_response.append(moon.to_dict())
    return moon_response



