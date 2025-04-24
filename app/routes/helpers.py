# from flask import abort, make_response
# from app.models.planets import planets

# # helper function to catch the errors
# def validate_planet(id):
#     try:
#         id = int(id)

#     except ValueError:
#         response = {"message": f"planet id should be a number"}
#         abort(make_response(response, 400))

#     for planet in planets:
#         if planet.id == int(id):
#             return planet
    
#     response = {"message": f"planet {id} not found"}
#     abort(make_response(response, 404))
