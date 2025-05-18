from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the conversion API!"}

def test_convert_c_to_f():
    response = client.post("/convert", json={"value": 0, "from_unit": "celsius", "to_unit": "fahrenheit"})
    assert response.status_code == 200
    assert response.json() == {"result": 30.0}

def test_invalid_units():
    response = client.post("/convert", json={"value": 100, "from_unit": "kelvin", "to_unit": "celsius"})
    assert response.status_code == 400

def test_missing_parameters():
    response = client.post("/convert", json={"value": 100})
    assert response.status_code == 422
