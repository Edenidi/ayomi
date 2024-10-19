from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_rpn_calculator_addition():
    response = client.post("/calculate/", json={"expression": "3 4 +"})
    assert response.status_code == 200
    assert response.json() == {"expression": "3 4 +", "result": 7}

def test_rpn_calculator_multiplication():
    response = client.post("/calculate/", json={"expression": "5 6 *"})
    assert response.status_code == 200
    assert response.json() == {"expression": "5 6 *", "result": 30}

def test_invalid_rpn_expression():
    response = client.post("/calculate/", json={"expression": "5 +"})
    assert response.status_code == 400
    assert "detail" in response.json()
