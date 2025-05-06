from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    size: Mapped[str]
    description: Mapped[str]


    def to_dict(self):
        moon_as_dict = {
            "id": self.id,
            "size": self.size,
            "description":self.description
        }
        return moon_as_dict
    
    @classmethod
    def from_dict(cls, moon_data):
        new_moon_instance = Moon(size=moon_data["size"], 
                                    description=moon_data["description"])
        return new_moon_instance

    
    def update_from_dict(self, moon_data):
        if "size" in moon_data:
            self.size = moon_data["size"]
        if "description" in moon_data:
            self.description = moon_data["description"]
