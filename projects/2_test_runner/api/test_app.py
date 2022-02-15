from apistar import test
from app import app, suites, SUITE_NOT_FOUND

client = test.TestClient(app)


def test_list_suites():
    response = client.get('/')
    assert response.status_code == 200
