from fastapi.testclient import TestClient
from app.main import app
from app.testing.logic import is_eligible_for_loan

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_loan_elgibility():
    assert is_eligible_for_loan(90000,22,"employed") == True
    assert is_eligible_for_loan(90000,20,"employed") == False