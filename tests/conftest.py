import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from dotenv import load_dotenv
import os
from app.models.planets import Planet
from app.models.moon import Moon

load_dotenv()

@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }
    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

# wave_7

@pytest.fixture
def two_saved_planets(app):
    # Arrange
    ocean_planet = Planet(name="Earth",
                    description="blue planet",
                    moons_n=1)
    mountain_planet = Planet(name="Mountain Planet",
                    description="i luv 2 climb rocks",
                    moons_n=1)

    db.session.add_all([ocean_planet, mountain_planet])
    # Alternatively, we could do
    # db.session.add(ocean_planet)
    # db.session.add(mountain_planet)
    db.session.commit()

    return [ocean_planet, mountain_planet]

# GET /planets/1 returns a response body that matches our fixture
@pytest.fixture
def planet_with_id_1(app):
    new_planet = Planet(id=1,
                    name="New",
                    description="green planet",
                    moons_n=5)
    db.session.add(new_planet)
    db.session.commit()

    return new_planet


