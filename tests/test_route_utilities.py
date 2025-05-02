from werkzeug.exceptions import HTTPException
from app.routes.helpers import validate_model
import pytest
from app.models.planets import Planet
...

def test_validate_planet(two_saved_planets):
    # Act
    result_planet = validate_model(Planet, 2)

    # Assert
    assert result_planet.id == 2
    assert result_planet.name == "Mountain Planet"
    assert result_planet.description == "i luv 2 climb rocks"
    assert result_planet.moons_n == 1

def test_validate_planet_missing_record(two_saved_planets):
    # Act & Assert
    # Calling `validate_planet` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException):
        result_planet = validate_model(Planet, "3")
    
def test_validate_planet_invalid_id(two_saved_planets):
    # Act & Assert
    # Calling `validate_planet` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException):
        result_planet = validate_model(Planet, "cat")