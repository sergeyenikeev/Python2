from fastapi.testclient import TestClient

def get_user_service_override():
    class FakeUserService:
        def list_users(self):
            return [{"id": 999, "name": "Test User"}]
    return FakeUserService()

app.dependency_overrides[get_user_service] = get_user_service_override

client = TestClient(app)

def test_list_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == [{"id": 999, "name": "Test User"}]