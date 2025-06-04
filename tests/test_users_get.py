import requests

def test_get_users_returns_200():
    response = requests.get("https://reqres.in/api/users?page=2")
    assert response.status_code == 200 

