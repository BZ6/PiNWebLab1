import pytest
from src.db.models import Schedule, User

def test_create_schedule(test_client, test_db_session):
    user_id = 1
    test_db_session.add(User(id=user_id, username="Test User", email="test@example.com"))
    test_db_session.commit()
    response = test_client.post("/schedules", json={
        "user_id": user_id,
        "date": "2023-10-01T12:00:00"
    })

    assert response.json()["status"] == 201
    assert response.json()["data"]["user_id"] == user_id
    assert response.json()["data"]["date"] == "2023-10-01T12:00:00"

def test_get_schedules(test_client, test_db_session):
    user_id = 1
    test_db_session.add(User(id=user_id, username="Test User", email="test@example.com"))
    test_db_session.commit()
    test_db_session.add_all([
        Schedule(id=1, user_id=user_id, date="2023-10-01T12:00:00"),
        Schedule(id=2, user_id=user_id, date="2023-10-01T12:00:00")
    ])
    test_db_session.commit()

    response = test_client.get("/schedules")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 2
    assert response.json()[0]["id"] == 1
    assert response.json()[1]["id"] == 2

def test_get_schedule(test_client, test_db_session):
    user_id = 1
    test_db_session.add(User(id=user_id, username="Test User", email="test@example.com"))
    test_db_session.commit()
    schedule_id = 1
    test_db_session.add(Schedule(id=schedule_id, user_id=user_id, date="2023-10-01T12:00:00"))
    test_db_session.commit()

    response = test_client.get(f"/schedules/{schedule_id}")

    assert response.status_code == 200
    assert response.json()["user_id"] == user_id
    assert response.json()["date"] == "2023-10-01T12:00:00"

def test_update_schedule(test_client, test_db_session):
    user_id = 1
    test_db_session.add_all([
        User(id=user_id, username="Test User 1", email="test1@example.com"),
        User(id=user_id + 1, username="Test User 2", email="test2@example.com")
    ])
    test_db_session.commit()
    schedule_id = 1
    test_db_session.add(Schedule(id=schedule_id, user_id=user_id + 1, date="2023-10-01T12:00:00"))
    test_db_session.commit()

    response = test_client.patch(f"/schedules/{schedule_id}", json={
        "user_id": user_id,
        "date": "2025-10-01T12:00:00"
    })

    assert response.status_code == 200
    assert response.json()["user_id"] == user_id
    assert response.json()["date"] == "2025-10-01T12:00:00"

def test_delete_schedule(test_client, test_db_session):
    user_id = 1
    test_db_session.add(User(id=user_id, username="Test User", email="test@example.com"))
    test_db_session.commit()
    schedule_id = 1
    test_db_session.add(Schedule(id=schedule_id, user_id=user_id, date="2023-10-01T12:00:00"))
    test_db_session.commit()

    response = test_client.delete(f"/schedules/{schedule_id}")

    assert response.status_code == 200
    assert response.json()["ok"] == True