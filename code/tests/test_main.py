from fastapi.testclient import TestClient
from app.main import app  

client = TestClient(app)

def test_read_root():
    response = client.get("/v1/recommendations/123")
    assert response.status_code == 200