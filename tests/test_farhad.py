from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_integer():
    response = client.post("/factorial", json=1)
    assert response.status_code == 200
    assert response.json() == 1

    response = client.post("/factorial", json=2)
    assert response.status_code == 200
    assert response.json() == 2

    response = client.post("/factorial", json=3)
    assert response.status_code == 200
    assert response.json() == 6

    response = client.post("/factorial", json=4)
    assert response.status_code == 200
    assert response.json() == 24

    response = client.post("/factorial", json=5)
    assert response.status_code == 200
    assert response.json() == 120

def test_string():
    response = client.post("/factorial", json="salam")
    assert response.status_code == 422

    response = client.post("/factorial", json="5")
    assert response.status_code == 200
    assert response.json() == 120

def test_none():
    response = client.post("/factorial", json=None)
    assert response.status_code == 422



