import pytest
from flask import request
from utils_flask_sqla.tests.utils import JSONClient, TestSession

from pypnnomenclature import create_app
from pypnnomenclature.env import db

db.session = db._make_scoped_session({"class_": TestSession})


@pytest.fixture(scope="session")
def _app():
    app = create_app()
    app.testing = True
    app.test_client_class = JSONClient

    @app.before_request
    def get_endpoint():
        pytest.endpoint = request.endpoint

    with app.app_context():
        yield app


@pytest.fixture(scope="session")
def _session(_app):
    return db.session


@pytest.fixture(scope="session", autouse=True)
def app(_app, _session):
    return _app
