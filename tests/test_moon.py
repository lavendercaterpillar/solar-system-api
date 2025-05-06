import pytest

def test_create_one_moon(client):
    # Act
    response = client.post("/moon", json={
        "description": "gray",
        "size":10000
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "description": "gray",
        "size":10000
    }

def test_get_one_moon_missing_record(client):
    # Act
    response = client.get("/moon/")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Moon not found"}