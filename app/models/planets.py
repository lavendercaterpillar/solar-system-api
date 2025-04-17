class Planet():
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

planets = [
    Planet(1, "Earth", "blue planet"),
    Planet(2, "Mercury", "grey planet"),
    Planet(3, "Venus", "golden brown planet"),
    Planet(4, "Mars", "red planet"),
    Planet(5, "Jupiter", "yellow, brown, red planet"),
    Planet(6, "Saturn", "yellow, brown, grey planet"),
    Planet(7, "Uranus", "cyan planet"),
    Planet(8, "Neptune", "blue"),
]