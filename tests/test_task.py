import pytest
from src.db.models import Priority, Task, User

def test_create_task(test_client, test_db_session):
    user_id = 1
    priority_id = 1
    test_db_session.add_all([
        User(id=user_id, username="User 1", email="user1@example.com"),
        Priority(id=priority_id, name="High")
    ])
    test_db_session.commit()
    response = test_client.post("/tasks", json={
        "user_id": user_id,
        "priority_id": priority_id,
        "description": "This is a test task",
        "deadline": "2023-12-31T23:59:59"
    })

    assert response.json()["status"] == 201
    assert response.json()["data"]["user_id"] == user_id
    assert response.json()["data"]["priority_id"] == priority_id
    assert response.json()["data"]["description"] == "This is a test task"
    assert response.json()["data"]["deadline"] == "2023-12-31T23:59:59"

def test_get_tasks(test_client, test_db_session):
    user_id = 1
    priority_id = 1
    test_db_session.add_all([
        User(id=user_id, username="User 1", email="user1@example.com"),
        Priority(id=priority_id, name="High")
    ])
    test_db_session.commit()
    test_db_session.add_all([
        Task(user_id=user_id, priority_id=priority_id, description="Description 1", deadline="2023-12-31T23:59:59"),
        Task(user_id=user_id, priority_id=priority_id, description="Description 2", deadline="2023-12-31T23:59:59")
    ])
    test_db_session.commit()

    response = test_client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 2
    assert response.json()[0]["description"] == "Description 1"
    assert response.json()[1]["description"] == "Description 2"

def test_get_task(test_client, test_db_session):
    user_id = 1
    priority_id = 1
    test_db_session.add_all([
        User(id=user_id, username="User 1", email="user1@example.com"),
        Priority(id=priority_id, name="High")
    ])
    test_db_session.commit()
    task_id = 1
    test_db_session.add(Task(id=task_id, user_id=user_id, priority_id=priority_id, description="This is a test task", deadline="2023-12-31T23:59:59"))
    test_db_session.commit()

    response = test_client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["user_id"] == user_id
    assert response.json()["priority_id"] == priority_id
    assert response.json()["description"] == "This is a test task"
    assert response.json()["deadline"] == "2023-12-31T23:59:59"

def test_update_task(test_client, test_db_session):
    user_id = 1
    priority_id = 1
    test_db_session.add_all([
        User(id=user_id, username="User 1", email="user1@example.com"),
        User(id=user_id + 1, username="User 2", email="user2@example.com"),
        Priority(id=priority_id, name="High"),
        Priority(id=priority_id + 1, name="Low")
    ])
    task_id = 1
    test_db_session.add(Task(id=task_id, user_id=user_id + 1, priority_id=priority_id + 1, description="This is a test task", deadline="2023-12-31T23:59:59"))
    test_db_session.commit()

    response = test_client.patch(f"/tasks/{task_id}", json={
        "user_id": user_id,
        "priority_id": priority_id,
        "description": "This is an updated task",
        "deadline": "2025-12-31T23:59:59"
    })

    assert response.status_code == 200
    assert response.json()["user_id"] == user_id
    assert response.json()["priority_id"] == priority_id
    assert response.json()["description"] == "This is an updated task"
    assert response.json()["deadline"] == "2025-12-31T23:59:59"

def test_delete_task(test_client, test_db_session):
    task_id = 1
    test_db_session.add(Task(id=task_id, description="This is a test task", deadline="2023-12-31T23:59:59"))
    test_db_session.commit()

    response = test_client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["ok"] == True