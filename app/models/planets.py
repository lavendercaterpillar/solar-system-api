from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    moons_n: Mapped[int]

    def to_dict(self):
        planet_dict = {}
        planet_dict["id"] = self.id
        planet_dict["name"] = self.name
        planet_dict["description"] = self.description
        planet_dict["moon_n"] = self.moon_n

        return planet_dict
    
    @classmethod
    def from_dict(cls, planet_data):
        new_planet_instance = Planet(name=planet_data["name"], 
                                    description=planet_data["description"],
                                    moons_n=planet_data["moons_n"])
        return new_planet_instance

    
    def update_from_dict(self, book_data):
        if "name" in book_data:
            self.title = book_data["name"]
        if "description" in book_data:
            self.description = book_data["description"]
        if "moons_n" in book_data:
            self.moons_n = book_data["moons_n"]



# class Planet():
#     def __init__(self, id, name, description):
#         self.id = id
#         self.name = name
#         self.description = description

# planets = [
#     Planet(1, "Earth", "blue planet"),
#     Planet(2, "Mercury", "grey planet"),
#     Planet(3, "Venus", "golden brown planet"),
#     Planet(4, "Mars", "red planet"),
#     Planet(5, "Jupiter", "yellow, brown, red planet"),
#     Planet(6, "Saturn", "yellow, brown, grey planet"),
#     Planet(7, "Uranus", "cyan planet"),
#     Planet(8, "Neptune", "blue"),
# ]