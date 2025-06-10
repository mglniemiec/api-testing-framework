import requests
from utils.schema_validator import validate_response

def test_get_user_returns_200(base_url):
    response = requests.get(f"{base_url}/users/2")
    assert response.status_code == 200
    validate_response(response.json(), "data/user_detail_schema.json")

def test_get_user_not_found_returns_404(base_url):
    response = requests.get(f"{base_url}/users/23")
    assert response.status_code == 404
    assert response.json() == {} 
