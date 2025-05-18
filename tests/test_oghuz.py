from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_sadedirmi():
    response = client.post("/prime", json={"number": 17})
    assert response.status_code == 200
    assert response.json() == {"result": "17 sade ədəddir."}

def test_deqiq_sadedir():
    response = client.post("/prime", json={"number": 32})
    assert response.status_code == 200
    assert response.json() == {"result": "32 sade ədəd deyil."}


def test_stringdirimi():
    response = client.post("/prime", json={"number": "salam"})
    assert response.status_code == 422

def test_bosdurmu():
    response = client.post("/prime", json={"number": None})
    assert response.status_code == 422
