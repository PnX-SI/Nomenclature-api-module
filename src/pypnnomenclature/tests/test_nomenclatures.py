import pytest
from flask import url_for

from utils_flask_sqla.tests.utils import JSONClient


@pytest.mark.usefixtures("client_class", "temporary_transaction")
class TestNomenclatures:
    def test_nomenclature_with_taxonomy_list(self):
        """Test retrieving the list of nomenclatures with taxonomy information."""
        response = self.client.get(url_for("nomenclatures.get_nomenclature_with_taxonomy_list"))
        assert response.status_code == 200
        assert len(response.json) > 0

    def test_nomenclature_list(self):
        """Test retrieving nomenclature list by code type."""
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
        """Test filtering nomenclatures by specific codes."""
        response = self.client.get(
            url_for("nomenclatures.get_nomenclature_by_type_list_and_taxonomy"),
            query_string={"cd_nomenclature": ["0", "1"], "code_type": "STADE_VIE"},
        )
        assert response.status_code == 200
        data = response.json[0]
        assert data["mnemonique"] == "STADE_VIE"
        assert len(data["values"]) == 2

    def test_nomenclature_list_with_hierarchy_filter(self):
        """Test filtering nomenclatures by hierarchy level."""
        response = self.client.get(
            url_for("nomenclatures.get_nomenclature_by_type_list_and_taxonomy"),
            query_string={"code_type": "STADE_VIE", "hierarchy": "0"},
        )
        assert response.status_code == 200
        data = response.json[0]
        assert data["mnemonique"] == "STADE_VIE"
        # Verify that all returned values have hierarchy starting with "0"
        if "values" in data and data["values"]:
            for value in data["values"]:
                assert value.get("hierarchy", "").startswith("0")

    def test_nomenclature_list_with_taxonomy_filters(self):
        """Test filtering nomenclatures by taxonomic kingdom (regne)."""
        response = self.client.get(
            url_for("nomenclatures.get_nomenclature_by_type_list_and_taxonomy"),
            query_string={
                "code_type": "STADE_VIE",
                "regne": "Animalia",
            },
        )
        assert response.status_code == 200
        data = response.json[0]
        assert data["mnemonique"] == "STADE_VIE"

    def test_nomenclature_list_with_multiple_taxonomy_filters(self):
        """Test filtering nomenclatures by multiple taxonomic levels (regne and group2_inpn)."""
        response = self.client.get(
            url_for("nomenclatures.get_nomenclature_by_type_list_and_taxonomy"),
            query_string={
                "code_type": "STADE_VIE",
                "regne": "Animalia",
                "group2_inpn": "Oiseaux",
            },
        )
        assert response.status_code == 200
        data = response.json[0]
        assert data["mnemonique"] == "STADE_VIE"

    def test_nomenclature_list_with_orderby_asc(self):
        """Test ordering nomenclatures in ascending order by label."""
        response = self.client.get(
            url_for("nomenclatures.get_nomenclature_by_type_list_and_taxonomy"),
            query_string={
                "code_type": "STADE_VIE",
                "orderby": "label_default",
                "order": "asc",
            },
        )
        assert response.status_code == 200
        data = response.json[0]
        assert data["mnemonique"] == "STADE_VIE"
        # Verify ascending order
        if "values" in data and len(data["values"]) > 1:
            labels = [v.get("label_default", "") for v in data["values"]]
            assert labels == sorted(labels)

    def test_nomenclature_list_with_orderby_desc(self):
        """Test ordering nomenclatures in descending order by label."""
        response = self.client.get(
            url_for("nomenclatures.get_nomenclature_by_type_list_and_taxonomy"),
            query_string={
                "code_type": "STADE_VIE",
                "orderby": "label_default",
                "order": "desc",
            },
        )
        assert response.status_code == 200
        data = response.json[0]
        assert data["mnemonique"] == "STADE_VIE"
        # Verify descending order
        if "values" in data and len(data["values"]) > 1:
            labels = [v.get("label_default", "") for v in data["values"]]
            assert labels == sorted(labels, reverse=True)

    def test_nomenclature_list_with_combined_filters(self):
        """Test combining code filters with ordering parameters."""
        response = self.client.get(
            url_for("nomenclatures.get_nomenclature_by_type_list_and_taxonomy"),
            query_string={
                "code_type": "STADE_VIE",
                "cd_nomenclature": ["0", "1"],
                "orderby": "cd_nomenclature",
                "order": "asc",
            },
        )
        assert response.status_code == 200
        data = response.json[0]
        assert data["mnemonique"] == "STADE_VIE"
        assert len(data["values"]) == 2
        # Verify order
        if "values" in data and len(data["values"]) > 1:
            codes = [v.get("cd_nomenclature", "") for v in data["values"]]
            assert codes == sorted(codes)
