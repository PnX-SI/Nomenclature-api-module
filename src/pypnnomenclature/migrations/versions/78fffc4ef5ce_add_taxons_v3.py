"""add taxons v3

Revision ID: 78fffc4ef5ce
Revises: 8eb9a12db289
Create Date: 2025-08-08 16:53:53.496062

"""

import importlib.resources

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision = "78fffc4ef5ce"
down_revision = "8eb9a12db289"
branch_labels = None
depends_on = None


def delete_nomenclatures(mnemonique):
    operation = text(
        """
            DELETE FROM ref_nomenclatures.t_nomenclatures
            WHERE id_type = (
                SELECT id_type
                FROM ref_nomenclatures.bib_nomenclatures_types
                WHERE mnemonique = :mnemonique
            );
            DELETE FROM ref_nomenclatures.bib_nomenclatures_types
            WHERE mnemonique = :mnemonique
        """
    )
    op.get_bind().execute(operation, {"mnemonique": mnemonique})


def upgrade():
    op.execute(
        importlib.resources.read_text(
            "pypnnomenclature.migrations.data", "nomenclatures_inpn_taxon_v3.sql"
        )
    )


def downgrade():
    delete_nomenclatures("SUPPORT_ORGANISM")
