from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    assert client.get("/health").status_code == 200

def test_factorial_valid():
    r = client.get("/factorial/5")
    assert r.json()["factorial"] == 120

def test_factorial_negative():
    assert client.get("/factorial/-1").status_code == 400

def test_factorial_overflow():
    assert client.get("/factorial/999").status_code == 400

def test_exp():
    r = client.get("/exp/1")
    assert abs(r.json()["result"] - 2.718) < 0.01