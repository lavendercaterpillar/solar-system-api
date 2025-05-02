from flask import abort, make_response
from app.models.planets import Planet   # helper function to catch the errors
from ..db import db



def validate_model(cls, model_id):
    try:
        id = int(model_id)    
    except ValueError:
        response = {"message": f"planet id should be a number"}
        abort(make_response(response, 400))

    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)    
    
    if not model:
        response = {"message": f"planet {model_id} not found"}
        abort(make_response(response, 404))

    return model
