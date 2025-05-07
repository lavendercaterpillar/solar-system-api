from app.models.planets import Planet
import pytest

def test_from_dict_returns_planet():
    # Arrange
    planet_data = {
        "name": "New Planet",
        "description": "The Best planet!",
        "moons_n": 4
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "New Planet"
    assert new_planet.description == "The Best planet!"
    assert new_planet.moons_n == 4

def test_from_dict_with_no_name():
    # Arrange
    planet_data = {
        "description": "The Best!"
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'name'):
        Planet.from_dict(planet_data)

def test_from_dict_with_no_description():
    # Arrange
    planet_data = {
        "name": "New Book"
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'description'):
        Planet.from_dict(planet_data)

def test_from_dict_with_extra_keys():
    # Arrange
    planet_data = {
        "extra": "some stuff",
        "name": "New Planet",
        "description": "The Best!",
        "moons_n": 4,
        "another": "last value"
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "New Planet"
    assert new_planet.description == "The Best!"
    assert new_planet.moons_n == 4

def test_to_dict_no_missing_data():
    # Arrange
    test_data = Planet(id = 1,
                    name="Blue planet",
                    description="watr 4evr",
                    moon = None,
                    moons_n=4)

    # Act
    result = test_data.to_dict()
    print(result)
    # Assert
    assert len(result) == 5
    assert result["id"] == 1
    assert result["name"] == "Blue planet"
    assert result["description"] == "watr 4evr"
    assert result["moons_n"] == 4
    assert result["moon"] == None


def test_to_dict_missing_id():
    # Arrange
    test_data = Planet(name="Blue planet",
                    description="watr 4evr",
                    moons_n=4,
                    moon = None)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] is None
    assert result["name"] == "Blue planet"
    assert result["description"] == "watr 4evr"
    assert result["moons_n"] == 4

def test_to_dict_missing_name():
    # Arrange
    test_data = Planet(id=1,
                    description="watr 4evr",
                    moons_n=4,
                    moon = None)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] == 1
    assert result["name"] is None
    assert result["description"] == "watr 4evr"
    assert result["moons_n"] == 4
    assert result["moon"] == None

def test_to_dict_missing_description():
    # Arrange
    test_data = Planet(id = 1,
                    name="Blue planet",
                    moons_n=4,
                    moon = None)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 5
    assert result["id"] == 1
    assert result["name"] == "Blue planet"
    assert result["description"] is None
    assert result["moons_n"] == 4
    assert result["moon"] == None