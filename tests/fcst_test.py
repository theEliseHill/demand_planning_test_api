from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# This is the test
def test_forecast_endpoint():
    response = client.post(
        "/forecast",
        json={
            "values": [100, 2, 80, 120, 90, 110, 95, 105],
            "window": 8
        }
    )

    assert response.status_code == 200
    assert "forecast" in response.json()