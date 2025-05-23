from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import Optional
from ..db import db

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .moon import Moon
class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    moons_n: Mapped[int]
    moon_id: Mapped[Optional[int]] = mapped_column(ForeignKey("moon.id"))
    moon: Mapped[Optional["Moon"]] = relationship(back_populates="planets")


    def to_dict(self):
        planet_dict = {}
        planet_dict["id"] = self.id
        planet_dict["name"] = self.name
        planet_dict["description"] = self.description
        planet_dict["moons_n"] = self.moons_n
            
        if self.moon:
            planet_dict["moon"] = self.moon.description
        else:
            planet_dict["moon"] = None

        return planet_dict
    
    @classmethod
    def from_dict(cls, planet_data):
        moon_id = planet_data.get("moon_id")

        new_planet_instance = cls(name=planet_data["name"], 
                                    description=planet_data["description"],
                                    moons_n=planet_data["moons_n"],
                                    moon_id=moon_id)
        
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