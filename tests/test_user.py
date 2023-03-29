from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
    
def test_read_user():
    response = client.get("/user2")
    assert response.status_code == 200
    assert response.json() == {"system": True}
    
def test_read_user2():
    response = client.get("/items/2?q=asdf")
    assert response.status_code == 200
    assert response.json() == {"item_id":2, "q": "asdf"}
