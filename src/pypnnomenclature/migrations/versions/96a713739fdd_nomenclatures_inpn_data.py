"""insert inpn data in ref_nomenclatures

Revision ID: 96a713739fdd
Revises:
Create Date: 2021-09-16 15:36:57.784074
"""

import importlib.resources

from alembic import op, context
import sqlalchemy as sa
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision = "96a713739fdd"
down_revision = None
branch_labels = ("nomenclatures_inpn_data",)
depends_on = ("6015397d686a",)  # ref_nomenclatures


def upgrade():
    op.execute(
        importlib.resources.read_text(
            "pypnnomenclature.migrations.data", "nomenclatures_inpn_data.sql"
        )
    )


# On supprime toutes les données de source GEONATURE, SINP & CAMPANULE
def downgrade():
    op.execute(
        """
    DELETE FROM ref_nomenclatures.defaults_nomenclatures_value dn USING ref_nomenclatures.t_nomenclatures n
    WHERE dn.id_nomenclature = n.id_nomenclature AND source in ('GEONATURE', 'SINP', 'CAMPANULE')
    """
    )
    op.execute(
        "DELETE FROM ref_nomenclatures.t_nomenclatures WHERE source in ('GEONATURE', 'SINP', 'CAMPANULE')"
    )
    op.execute(
        "DELETE FROM ref_nomenclatures.bib_nomenclatures_types WHERE source in ('GEONATURE', 'SINP', 'CAMPANULE')"
    )
