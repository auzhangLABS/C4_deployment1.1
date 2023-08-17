from app import app


def test_home_page():
    response = application.test_client().get('/')
    assert response.status_code == 200
