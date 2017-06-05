import pytest
from expecter import expect

from webcalc import app, mongo


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def pattern():
    with app.app_context():
        mongo.db.operations.drop()
        mongo.db.operations.insert(
            dict(
                name="+",
                pattern="{{ a + b }}"
            )
        )


def describe_index():

    def it_says_hello(client):
        response = client.get('/')

        expect(response.data).contains(b"Bell's Hopslam")


def describe_calc():

        def when_plus(client, pattern):
            response = client.get('/4/+/5')

            expect(response.data).contains(b"9")
