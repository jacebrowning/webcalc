import pytest
from expecter import expect

from webcalc import app


@pytest.fixture
def client():
    return app.test_client()


def describe_index():

    def it_says_hello(client):
        response = client.get('/')

        expect(response.data).contains(b"Bell's Hopslam")
