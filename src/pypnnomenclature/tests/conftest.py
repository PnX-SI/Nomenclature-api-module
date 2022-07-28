import pytest

from pypnnomenclature import create_app
from pypnnomenclature.env import db


@pytest.fixture(scope="session")
def app():
    return create_app()


@pytest.fixture(scope="session")
def _session(app):
    return db.session
