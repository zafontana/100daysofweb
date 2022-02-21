from apistar import test
from app import app, suites, SUITE_NOT_FOUND

client = test.TestClient(app)


def test_list_get200():
    response = client.get('/')
    assert response.status_code == 200


def test_list_count():
    response = client.get('/')

    json_resp = response.json()
    suites_count = len(suites)
    assert len(json_resp) == suites_count


def test_create_suite():
    suite_count = len(suites)
    data = {
        "suite_name": "pytest create suite",
        "suite_description": "abd"
    }

    response = client.post('/', data=data)

    assert response.status_code == 201, "Status code is 201."
    assert len(suites) == suite_count + 1, "Count of suites increased by 1."

    response = client.get('/11/')
    expected = {
        "id": 11,
        "suite_name": "pytest create suite",
        "suite_description": "abd"
    }
    assert response.json() == expected, "GET request JSON is as expected."


def test_create_ignores_id():
    suite_count = len(suites)
    data = {
        "id": 20,
        "suite_name": "pytest create suite",
        "suite_description": "abd"
    }

    response = client.post('/', data=data)

    assert response.status_code == 201, "Status code is 201."
    assert len(suites) == suite_count + 1, "Count of suites increased by 1."

    response = client.get('/11/')
    expected = {
        "id": 11,
        "suite_name": "pytest create suite",
        "suite_description": "abd"
    }
    assert response.json() == expected, "GET request JSON is as expected."


def test_create_name_too_long():
    suite_count = len(suites)
    data = {
        "id": 20,
        "suite_name": "pytest create suite with extremely long name bla bla bla",
        "suite_description": "abd"
    }

    response = client.post('/', data=data)

    assert response.status_code == 400, "Status code is 400."
    assert response.json()["suite_name"] == "Must have no more than 50 characters.", "Error message is 'Must have no more than 50 characters.'"
    assert len(suites) == suite_count, "Count of suites didn't increase."


def test_suite_not_found():
    response = client.get('/123/')
    assert response.status_code == 404
    assert response.json() == {'error': SUITE_NOT_FOUND}
