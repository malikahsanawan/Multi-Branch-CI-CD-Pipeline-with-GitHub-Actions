from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_root_returns_ok():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_echo_returns_same_message():
    payload = {"message": "hello fastapi"}
    response = client.post("/echo", json=payload)
    assert response.status_code == 200
    assert response.json() == {"echo": payload["message"]}

