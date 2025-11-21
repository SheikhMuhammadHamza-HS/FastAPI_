from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_hello_msg():
  response = client.get("/")
  assert response.status_code == 200
  assert response.json() == {"message": "Hellow hey"}
  
def test_start_chat():
  response = client.post("/chat/start", json={"message": "Hello"})
  assert response.status_code == 200
    