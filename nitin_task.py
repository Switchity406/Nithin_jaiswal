import requests
import pytest

# API endpoints
GET_USERS_URL = "https://reqres.in/api/users"
CREATE_USER_URL = "https://reqres.in/api/users"
UPDATE_USER_URL = "https://reqres.in/api/users/{id}"

# Test data
NEW_USER_DATA = {
    "name": "John Doe",
    "job": "Engineer"
}
UPDATE_USER_DATA = {
    "name": "John Smith",
    "job": "Developer"
}


@pytest.fixture(scope="session")
def api_client():
    return requests.Session()


# Test GET /users endpoint
def test_get_users(api_client):
    response = api_client.get(GET_USERS_URL, params={"page": 1})
    assert response.status_code == 200

    data = response.json()["data"]
    for user in data:
        assert "email" in user
        assert "first_name" in user


def test_get_user_by_id(api_client):
    # Create a new user and retrieve the ID
    response = api_client.post(CREATE_USER_URL, json=NEW_USER_DATA)
    assert response.status_code == 201

    user_id = response.json()["id"]

    # Get the user by ID and validate the response
    response = api_client.get(UPDATE_USER_URL.format(id=user_id))
    assert response.status_code == 200

    user_data = response.json()["data"]
    assert user_data["id"] == user_id

    # Delete the user after the test
    response = api_client.delete(UPDATE_USER_URL.format(id=user_id))
    assert response.status_code == 204


def test_create_user(api_client):
    # Create a new user and validate the response
    response = api_client.post(CREATE_USER_URL, json=NEW_USER_DATA)
    assert response.status_code == 201

    user_data = response.json()
    assert "id" in user_data
    assert user_data["name"] == NEW_USER_DATA["name"]
    assert user_data["job"] == NEW_USER_DATA["job"]

    # Delete the user after the test
    response = api_client.delete(UPDATE_USER_URL.format(id=user_data["id"]))
    assert response.status_code == 204


def test_update_user(api_client):
    # Create a new user and retrieve the ID
    response = api_client.post(CREATE_USER_URL, json=NEW_USER_DATA)
    assert response.status_code == 201

    user_id = response.json()["id"]

    # Update the user data and validate the response
    response = api_client.put(UPDATE_USER_URL.format(id=user_id), json=UPDATE_USER_DATA)
    assert response.status_code == 200

    updated_user_data = response.json()
    assert updated_user_data["name"] == UPDATE_USER_DATA["name"]
    assert updated_user_data["job"] == UPDATE_USER_DATA["job"]

    # Delete the user after the test
    response = api_client.delete(UPDATE_USER_URL.format(id=user_id))
    assert response.status_code == 204
