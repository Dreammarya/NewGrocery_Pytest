import pytest
import requests

Base_url = "http://jsonplaceholder.typicode.com"


def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert len(response.json()) > 0

@pytest.mark.parametrize("id, expected_status, expected_id", [
    (2, 200,2),
    (1,200,2)
])
def test_get_single_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_create_post():
    new_post = {
        "title": "Pytest guide",
        "body": "Learning api testing with pytest",
        "userId": 1
    }
    response = requests.post(f"{Base_url}/post/1")
