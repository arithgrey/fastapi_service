from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    user_data = {"email": "test@example.com", "password": "123456"}
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    created_user = response.json()
    assert created_user["email"] == user_data["email"]


def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    users = response.json()
    assert len(users) > 0


def test_read_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    user = response.json()
    assert "id" in user
    assert "email" in user


def test_create_item_for_user():
    item_data = {"name": "Test Item", "description": "Test Description"}
    response = client.post("/users/1/items/", json=item_data)
    assert response.status_code == 200
    created_item = response.json()
    assert created_item["name"] == item_data["name"]


def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    items = response.json()
    assert len(items) > 0
