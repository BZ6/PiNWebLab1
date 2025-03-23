import pytest
from models.models import Schedule, ScheduleTask, Task

def test_create_schedule_task(test_client, test_db_session):
    schedule_id = 1
    task_id = 1
    test_db_session.add_all([
        Task(id=task_id, description="Description 1", deadline="2023-12-31T23:59:59"),
        Schedule(id=schedule_id, date="2023-10-01T12:00:00")
    ])
    response = test_client.post(f"/schedule_tasks/{schedule_id}/{task_id}")

    assert response.json()["status"] == 201
    assert response.json()["data"]["schedule_id"] == schedule_id
    assert response.json()["data"]["task_id"] == task_id

def test_get_schedule_tasks(test_client, test_db_session):
    test_db_session.add_all([
        Task(id=1, description="Description 1", deadline="2023-12-31T23:59:59"),
        Task(id=2, description="Description 2", deadline="2023-12-31T23:59:59"),
        Schedule(id=1, date="2023-10-01T12:00:00"),
        Schedule(id=2, date="2023-10-01T12:00:00")
    ])
    test_db_session.commit()
    test_db_session.add_all([
        ScheduleTask(schedule_id=1, task_id=1),
        ScheduleTask(schedule_id=2, task_id=2)
    ])
    test_db_session.commit()

    response = test_client.get("/schedule_tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 2
    assert response.json()[0]["schedule_id"] == 1
    assert response.json()[1]["schedule_id"] == 2

def test_get_schedule_task(test_client, test_db_session):
    schedule_id = 1
    task_id = 1
    test_db_session.add_all([
        Task(id=task_id, description="Description 1", deadline="2023-12-31T23:59:59"),
        Schedule(id=schedule_id, date="2023-10-01T12:00:00")
    ])
    test_db_session.commit()
    test_db_session.add(ScheduleTask(schedule_id=schedule_id, task_id=task_id))
    test_db_session.commit()

    response = test_client.get(f"/schedule_tasks/{schedule_id}/{task_id}")

    assert response.status_code == 200
    assert response.json()["schedule_id"] == schedule_id
    assert response.json()["task_id"] == task_id

def test_delete_schedule_task(test_client, test_db_session):
    schedule_id = 1
    task_id = 1
    test_db_session.add_all([
        Task(id=task_id, description="Description 1", deadline="2023-12-31T23:59:59"),
        Schedule(id=schedule_id, date="2023-10-01T12:00:00")
    ])
    test_db_session.commit()
    test_db_session.add(ScheduleTask(schedule_id=schedule_id, task_id=task_id))
    test_db_session.commit()

    response = test_client.delete(f"/schedule_tasks/{schedule_id}/{task_id}")

    assert response.status_code == 200
    assert response.json()["ok"] == True