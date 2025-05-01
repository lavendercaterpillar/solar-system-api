from app.db import db
from app.models.planets import Planet


# Create a test to check GET /planets returns 200 and an empty array.
def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


# 1. GET /planets/1 returns a response body that matches our fixture
def test_planet_with_id_1(client, planet_with_id_1):
    response = client.get(f"/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body["id"] == planet_with_id_1.id
    assert response_body["name"] == planet_with_id_1.name
    assert response_body["description"] == planet_with_id_1.description
    assert response_body["moons_n"] == planet_with_id_1.moons_n

# 2. GET /planets/1 with no data in test database (no fixture) returns a 404
def test_planet_with_no_id_1(client):
    response = client.get(f"/planets/1")
    # Assert
    assert response.status_code == 404


# 3..GET /planets with valid test data (fixtures) returns a 200 with an array including appropriate test data
def test_get_two_planets(client, two_saved_planets):
    # Act
    response = client.get(f"/planets")
    response_body = response.get_json()

    # Assert
    fixture_json = []
    for saved_planet in two_saved_planets:
        fixture_json.append({
            "id": saved_planet.id,
            "name": saved_planet.name,
            "description": saved_planet.description,
            "moons_n": saved_planet.moons_n
        })
    #print(two_saved_planets)
    #print(fixture_json)
    #assert False
    assert response.status_code == 200
    assert fixture_json == response_body

# 4. POST /planets with a JSON request body returns a 201
def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "New planet",
        "description": "The Best!",
        "moons_n":2
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "New planet",
        "description": "The Best!",
        "moons_n":2
    }
# ..GET /one/planet with valid test data (fixtures) returns a 200 with an array including appropriate test data
def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Earth",
        "description": "blue planet",
        "moons_n":1
    }