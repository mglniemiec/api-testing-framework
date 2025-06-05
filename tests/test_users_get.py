import requests
from utils.schema_validator import validate_response


def test_get_users_returns_200(base_url):
    response = requests.get(f"{base_url}/users?page=2")
    assert response.status_code == 200
    validate_response(response.json(), "data/user_list_schema.json") 
	
