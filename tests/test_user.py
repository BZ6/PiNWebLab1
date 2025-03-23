import pytest
from src.db.models import User

def test_create_user(test_client, test_db_session):
    response = test_client.post("/users", json={
        "username": "Test User",
        "email": "test@example.com"
    })

    assert response.json()["status"] == 201
    assert response.json()["data"]["username"] == "Test User"
    assert response.json()["data"]["email"] == "test@example.com"


def test_get_users(test_client, test_db_session):
    test_db_session.add_all([
        User(username="User 1", email="user1@example.com"),
        User(username="User 2", email="user2@example.com")
    ])
    test_db_session.commit()

    response = test_client.get("/users")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 2
    assert response.json()[0]["username"] == "User 1"
    assert response.json()[1]["username"] == "User 2"

def test_get_user(test_client, test_db_session):
    user_id = 1
    test_db_session.add(User(id=user_id, username="Test User", email="test@example.com"))
    test_db_session.commit()

    response = test_client.get(f"/users/{user_id}")

    assert response.status_code == 200
    assert response.json()["username"] == "Test User"
    assert response.json()["email"] == "test@example.com"

def test_update_user(test_client, test_db_session):
    user_id = 1
    test_db_session.add(User(id=user_id, username="Test User", email="test@example.com"))
    test_db_session.commit()

    response = test_client.patch(f"/users/{user_id}", json={
        "username": "Updated User",
        "email": "updated@example.com"
    })

    assert response.status_code == 200
    assert response.json()["username"] == "Updated User"
    assert response.json()["email"] == "updated@example.com"

def test_delete_user(test_client, test_db_session):
    user_id = 1
    test_db_session.add(User(id=user_id, username="Test User", email="test@example.com"))
    test_db_session.commit()

    response = test_client.delete(f"/users/{user_id}")

    assert response.status_code == 200
    assert response.json()["ok"] == True