from fastapi.testclient import TestClient  # TestClient is used to create the test context
from app.main import app

client = TestClient(app)

# this is an integration test
def test_loan_eligbitly():
    payload = {
        "income": 90000,
        "age": 30,
        "employee_status": "employed"
    }
    response = client.post("/loan-eligibility", json=payload)
    assert response.status_code == 200
    assert response.json() == {
        "eligibility_status": True
    }

# this is validation error
def test_loan_eligibility_invalid_payload():
    response = client.post("/loan-eligibility", json={"income": "abc"})
    assert response.status_code == 422

# in a realw rold scenrio you would have
# tests/
#     test_loan/
#         test_positive_scenarios.py
#         test_negative_scenarios.py

