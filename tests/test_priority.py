import pytest
from models.models import Priority

def test_create_priority(test_client, test_db_session):
    response = test_client.post("/priorities", json={
        "name": "High"
    })

    assert response.json()["status"] == 201
    assert response.json()["data"]["name"] == "High"

def test_get_priorities(test_client, test_db_session):
    test_db_session.add_all([
        Priority(name="High"),
        Priority(name="Medium")
    ])
    test_db_session.commit()

    response = test_client.get("/priorities")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 2
    assert response.json()[0]["name"] == "High"
    assert response.json()[1]["name"] == "Medium"

def test_get_priority(test_client, test_db_session):
    priority_id = 1
    test_db_session.add(Priority(id=priority_id, name="High"))
    test_db_session.commit()

    response = test_client.get(f"/priorities/{priority_id}")

    assert response.status_code == 200
    assert response.json()["name"] == "High"

def test_update_priority(test_client, test_db_session):
    priority_id = 1
    test_db_session.add(Priority(id=priority_id, name="High"))
    test_db_session.commit()

    response = test_client.patch(f"/priorities/{priority_id}", json={
        "name": "Updated Priority"
    })

    assert response.status_code == 200
    assert response.json()["name"] == "Updated Priority"

def test_delete_priority(test_client, test_db_session):
    priority_id = 1
    test_db_session.add(Priority(id=priority_id, name="High"))
    test_db_session.commit()

    response = test_client.delete(f"/priorities/{priority_id}")

    assert response.status_code == 200
    assert response.json()["ok"] == True