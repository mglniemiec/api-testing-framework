import requests

def test_get_users_returns_200(base_url):
    response = requests.get(f"{base_url}/users?page=2")
    assert response.status_code == 200 

