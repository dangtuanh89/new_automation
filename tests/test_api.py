import pytest
from helper.api_helper import APIHelper

@pytest.fixture
def api():
    return APIHelper()

class TestAPI:
    
    def test_get_user_information(self, api):
        response = api.get("/users/2")
        assert response.status_code == 200, f'Expected status code 200, but got {response.status_code}'
        print('Status code: ', response.status_code)

        data = response.json()
        print('Response Json:', data)

        self.validate_user_information(
            data["data"],
            expected_id=2,
            expected_email="janet.weaver@reqres.in",
            expected_first_name="Janet",
            expected_last_name="Weaver"
        )
    
    def validate_user_information(self, user_data, expected_id = None, expected_email = None, expected_first_name = None, expected_last_name = None):
        assert user_data["id"] == expected_id, f'Expected id: {expected_id}, got {user_data["id"]}'
        if expected_email:
            assert user_data["email"] == expected_email, f'Expected email: {expected_email}, got: {user_data["email"]}'
        if expected_first_name:
            assert user_data["first_name"] == expected_first_name, f'Expected first_name: {expected_first_name}, got: {user_data["first_name"]}'
        if expected_last_name:
            assert user_data["last_name"] == expected_last_name, f'Expected last_name: {expected_last_name}, got: {user_data["last_name"]}'

    def test_create_user(self, api):
        payload = {
            "name": "morpheus",
            "job": "leader"
        }
        response = api.post("/users", data=payload)
    
        assert response.status_code == 201
    
        # Kiểm tra dữ liệu trả về
        data = response.json()
        assert data["name"] == "morpheus"
        assert data["job"] == "leader"
