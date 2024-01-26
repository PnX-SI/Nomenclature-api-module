"""insert taxonomic filtering data in ref_nomenclatures.cor_taxref_nomenclatures

Revision ID: a763fb554ff2
Revises:
Create Date: 2021-09-16 15:36:57.784074
"""

import importlib.resources

from alembic import op
import sqlalchemy as sa
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import CheckViolation


# revision identifiers, used by Alembic.
revision = "a763fb554ff2"
down_revision = None
branch_labels = ("nomenclatures_taxonomie_data",)
depends_on = (
    "f5436084bf17",  # nomenclatures_taxonomie
    "96a713739fdd",  # nomenclatures_inpn_data
)


def upgrade():
    try:
        op.execute(
            importlib.resources.read_text(
                "pypnnomenclature.migrations.data",
                "nomenclatures_taxonomie_data.sql",
            )
        )
    except IntegrityError as exc:
        if type(exc.orig) == CheckViolation and exc.orig.diag.constraint_name in [
            "check_cor_taxref_nomenclature_isregne",
            "check_cor_taxref_nomenclature_isgroup2inpn",
        ]:
            raise Exception(
                "Avez-vous bien préalablement inséré le référentiel TaxRef dans votre base de données ?"
            ) from exc
        else:
            raise


def downgrade():
    # WARNING: we do not check cor_taxref_nomenclature contains only INPN data…
    # If you are not sure, delete unwanted data manually and then stamp previous revision.
    op.execute("TRUNCATE TABLE ref_nomenclatures.cor_taxref_nomenclature")
