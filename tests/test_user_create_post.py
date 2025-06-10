import requests

def test_create_user_returns_201(base_url):
    payload = {
        "name": "max",
        "job": "leader"
    }
    response = requests.post(f"{base_url}/users", json=payload)
    assert response.status_code == 201
    json_data = response.json()
    assert json_data["name"] == "max"
    assert json_data["job"] == "leader"
    assert "id" in json_data
    assert "createdAt" in json_data

