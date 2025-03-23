import pytest
from src.db.models import Notification, Task

def test_create_notification(test_client, test_db_session):
    task_id = 1
    test_db_session.add(Task(id=task_id, description="Description 1", deadline="2023-12-31T23:59:59"))
    test_db_session.commit()
    response = test_client.post("/notifications", json={
        "task_id": task_id,
        "message": "Test Notification",
        "sent_at": "2023-10-01T12:00:00Z"
    })

    assert response.json()["status"] == 201
    assert response.json()["data"]["task_id"] == task_id
    assert response.json()["data"]["message"] == "Test Notification"

def test_get_notifications(test_client, test_db_session):
    task_id = 1
    test_db_session.add(Task(id=task_id, description="Description 1", deadline="2023-12-31T23:59:59"))
    test_db_session.commit()
    test_db_session.add_all([
        Notification(task_id=task_id, message="Notification 1", sent_at="2023-10-01T12:00:00Z"),
        Notification(task_id=task_id, message="Notification 2", sent_at="2023-10-01T12:00:00Z")
    ])
    test_db_session.commit()

    response = test_client.get("/notifications")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 2
    assert response.json()[0]["message"] == "Notification 1"
    assert response.json()[1]["message"] == "Notification 2"

def test_get_notification(test_client, test_db_session):
    task_id = 1
    test_db_session.add(Task(id=task_id, description="Description 1", deadline="2023-12-31T23:59:59"))
    test_db_session.commit()
    notification_id = 1
    test_db_session.add(Notification(id=notification_id, task_id=task_id, message="Test Notification", sent_at="2023-10-01T12:00:00Z"))
    test_db_session.commit()

    response = test_client.get(f"/notifications/{notification_id}")

    assert response.status_code == 200
    assert response.json()["task_id"] == task_id
    assert response.json()["message"] == "Test Notification"
    assert response.json()["sent_at"] == "2023-10-01T12:00:00"

def test_update_notification(test_client, test_db_session):
    task_id = 1
    test_db_session.add_all([
        Task(id=task_id, description="Description 1", deadline="2023-12-31T23:59:59"),
        Task(id=task_id + 1, description="Description 2", deadline="2023-12-31T23:59:59")
    ])
    test_db_session.commit()
    notification_id = 1
    test_db_session.add(Notification(id=notification_id, task_id=task_id + 1, message="Test Notification", sent_at="2023-10-01T12:00:00Z"))
    test_db_session.commit()

    response = test_client.patch(f"/notifications/{notification_id}", json={
        "task_id": task_id,
        "message": "Updated Notification",
        "sent_at": "2023-10-01T12:00:00Z"
    })

    assert response.status_code == 200
    assert response.json()["task_id"] == task_id
    assert response.json()["message"] == "Updated Notification"

def test_delete_notification(test_client, test_db_session):
    task_id = 1
    test_db_session.add(Task(id=task_id, description="Description 1", deadline="2023-12-31T23:59:59"))
    test_db_session.commit()
    notification_id = 1
    test_db_session.add(Notification(id=notification_id, task_id=task_id, message="Test Notification", sent_at="2023-10-01T12:00:00Z"))
    test_db_session.commit()

    response = test_client.delete(f"/notifications/{notification_id}")

    assert response.status_code == 200
    assert response.json()["ok"] == True