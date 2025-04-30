def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_two_planet(client, two_saved_planets):
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