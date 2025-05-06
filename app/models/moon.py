from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .planets import Planet

class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    size: Mapped[int]
    description: Mapped[str]
    planets: Mapped[list["Planet"]] = relationship(back_populates="moon")


    def to_dict(self):
        moon_as_dict = {
            "id": self.id,
            "size": self.size,
            "description":self.description
        }
        return moon_as_dict
    
    @classmethod
    def from_dict(cls, moon_data):
        new_moon_instance = cls(size=moon_data["size"], 
                                    description=moon_data["description"])
        return new_moon_instance

    
    def update_from_dict(self, moon_data):
        if "size" in moon_data:
            self.size = moon_data["size"]
        if "description" in moon_data:
            self.description = moon_data["description"]
