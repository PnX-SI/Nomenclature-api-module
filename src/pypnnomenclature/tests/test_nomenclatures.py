import pytest
from flask import url_for

from utils_flask_sqla.tests.utils import JSONClient


@pytest.mark.usefixtures("client_class", "temporary_transaction")
class TestNomenclatures:
    def test_nomenclature_with_taxonomy_list(self):
        response = self.client.get(url_for("nomenclatures.get_nomenclature_with_taxonomy_list"))
        assert response.status_code == 200
        assert len(response.json) > 0
