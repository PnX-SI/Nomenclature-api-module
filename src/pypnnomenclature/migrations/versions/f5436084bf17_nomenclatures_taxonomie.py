"""add support for taxonomy into ref_nomenclatures

Revision ID: f5436084bf17
Create Date: 2021-09-16 15:08:57.784074

"""

import importlib.resources

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f5436084bf17"
down_revision = None
branch_labels = ("nomenclatures_taxonomie",)
depends_on = (
    "6015397d686a",  # ref_nomenclatures
    "9c2c0254aadc",  # taxonomie
)


def upgrade():
    op.execute(
        importlib.resources.read_text(
            "pypnnomenclature.migrations.data", "nomenclatures_taxonomie.sql"
        )
    )


def downgrade():
    op.execute(
        """
    DROP VIEW ref_nomenclatures.v_meth_determin;
    DROP VIEW ref_nomenclatures.v_sampling_units_typ;
    DROP VIEW ref_nomenclatures.v_sampling_plan_typ;
    DROP VIEW ref_nomenclatures.v_data_typ;
    DROP VIEW ref_nomenclatures.v_resource_typ;
    DROP VIEW ref_nomenclatures.v_niv_precis;
    DROP VIEW ref_nomenclatures.v_statut_valid;
    DROP VIEW ref_nomenclatures.v_statut_obs;
    DROP VIEW ref_nomenclatures.v_preuve_exist;
    DROP VIEW ref_nomenclatures.v_naturalite;
    DROP VIEW ref_nomenclatures.v_statut_bio;
    DROP VIEW ref_nomenclatures.v_meth_obs;
    DROP VIEW ref_nomenclatures.v_type_denbr;
    DROP VIEW ref_nomenclatures.v_objet_denbr;
    DROP VIEW ref_nomenclatures.v_sexe;
    DROP VIEW ref_nomenclatures.v_stade_vie;
    DROP VIEW ref_nomenclatures.v_eta_bio;
    DROP VIEW ref_nomenclatures.v_technique_obs;
    DROP VIEW ref_nomenclatures.v_nomenclature_taxonomie;

    DROP TABLE ref_nomenclatures.cor_taxref_nomenclature;
    DROP FUNCTION ref_nomenclatures.get_filtered_nomenclature(character varying, character varying, character varying)
    """
    )
