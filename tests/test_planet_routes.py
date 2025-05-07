import pytest

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
    # assert response_body["moons_n"] == planet_with_id_1.moons_n

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
            "moons_n": saved_planet.moons_n,
            "moon": saved_planet.moon
        })
    # print(two_saved_planets)
    # print(fixture_json)
    # assert False
    assert response.status_code == 200
    assert fixture_json == response_body

# 4. POST /planets with a JSON request body returns a 201
def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "New planet",
        "description": "The Best!",
        "moons_n":2,
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "New planet",
        "description": "The Best!",
        "moons_n":2,
        "moon": None
    }

# 3..GET /one/planet with valid test data (fixtures) returns a 200 with an array including appropriate test data
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
        "moons_n":1,
        "moon": None
    }


# wave_7

def test_create_one_planet_no_name(client):
    # Arrange
    test_data = {"description": "The Best!"}

    # Act
    response = client.post("/planets", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {'message': 'Invalid request: missing name'}

def test_create_one_planet_no_description(client):
    # Arrange
    test_data = {"name": "New Planet"}

    # Act
    response = client.post("/planets", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {'message': 'Invalid request: missing description'}

def test_create_one_planet_with_extra_keys(client):
    # Arrange
    test_data = {
        "extra": "some stuff",
        "name": "New Planet",
        "description": "The Best!",
        "another": "last value",
        "moons_n": 4
    }

    # Act
    response = client.post("/planets", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "New Planet",
        "description": "The Best!",
        "moons_n": 4,
        "moon": None
    }

# When we have records and a `name` query in the request arguments, `get_all_planets` returns a list containing only the `Planet`s that match the query
def test_get_all_planets_with_name_query_matching_none(client, two_saved_planets):
    # Act
    data = {'name': 'Desert Planet'}
    response = client.get("/planets", query_string = data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

# When we have records and a `name` query in the request arguments, `get_all_planets` returns a list containing only the `Planet`s that match the query
def test_get_all_planets_with_name_query_matching_one(client, two_saved_planets):
    # Act
    data = {'name': 'Earth'}
    response = client.get("/planets", query_string = data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0] == {
        "id": 1,
        "name": "Earth",
        "description": "blue planet",
        "moons_n": 1,
        "moon": None
    }

# When we call `get_one_planet` with a numeric ID that doesn't have a record, we get the expected error message
def test_get_one_planet_missing_record(client, two_saved_planets):
    # Act
    response = client.get("/planets/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Planet 3 not found"}

# When we call `get_one_planet` with a non-numeric ID, we get the expected error message
def test_get_one_planet_invalid_id(client, two_saved_planets):
    # Act
    response = client.get("/planets/cat")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message": "Planet cat invalid"}

def test_update_planet(client, two_saved_planets):
    # Arrange
    test_data = {
        "name": "New planet",
        "description": "The Best!",
        "moons_n": 5
    }

    # Act
    response = client.put("/planets/1", json=test_data)
    #response_body = response.get_json()

    # Assert
    assert response.status_code == 204
    assert response.content_length is None


def test_update_planet_with_extra_keys(client, two_saved_planets):
    # Arrange
    test_data = {
        "extra": "some stuff",
        "name": "New planet",
        "description": "The Best!",
        "moons_n": 5,
        "another": "last value"
    }

    # Act
    response = client.put("/planets/1", json=test_data)

    # Assert
    assert response.status_code == 204
    assert response.content_length is None


def test_update_planet_invalid_id(client, two_saved_planets):
    # Arrange
    test_data = {
        "name": "New planet",
        "description": "The Best!",
        "moons_n": 5
    }

    # Act
    response = client.put("/planets/cat", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message": "Planet cat invalid"}

def test_update_planet_missing_record(client, two_saved_planets):
    # Arrange
    test_data = {
        "name": "New Planet",
        "description": "The Best!",
        "moons_n": 5

    }

    # Act
    response = client.put("/planets/3", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Planet 3 not found"}

def test_update_planet_invalid_id(client, two_saved_planets):
    # Arrange
    test_data = {
        "name": "New Planet",
        "description": "The Best!",
        "moons_n": 5
    }

    # Act
    response = client.put("/planets/cat", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message": "Planet cat invalid"}

def test_delete_planet(client, two_saved_planets):
    # Act
    response = client.delete("/planets/1")

    # Assert
    assert response.status_code == 204
    assert response.content_length is None

def test_delete_planet_missing_record(client, two_saved_planets):
    # Act
    response = client.delete("/planets/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Planet 3 not found"}

def test_delete_planet_invalid_id(client, two_saved_planets):
    # Act
    response = client.delete("/planets/cat")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message": "Planet cat invalid"}