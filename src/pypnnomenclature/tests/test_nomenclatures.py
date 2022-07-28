import pytest
from flask import url_for

from utils_flask_sqla.tests.utils import JSONClient


@pytest.mark.usefixtures("client_class", "temporary_transaction")
class TestNomenclatures:
    def test_nomenclature_with_taxonomy_list(self):
        response = self.client.get(url_for("nomenclatures.get_nomenclature_with_taxonomy_list"))
        assert response.status_code == 200
        assert len(response.json) > 0

    def test_nomenclature_list(self):
        response = self.client.get(
            url_for(
                "nomenclatures.get_nomenclature_by_mnemonique_and_taxonomy",
                code_type="STADE_VIE",
            )
        )
        assert response.status_code == 200
        data = response.json
        assert data["mnemonique"] == "STADE_VIE"

    def test_nomenclature_list_with_filters(self):
        response = self.client.get(
            url_for("nomenclatures.get_nomenclature_by_type_list_and_taxonomy"),
            query_string={"cd_nomenclature": ["0", "1"], "code_type": "STADE_VIE"},
        )
        assert response.status_code == 200
        data = response.json[0]
        assert data["mnemonique"] == "STADE_VIE"
        assert len(data["values"]) == 2
