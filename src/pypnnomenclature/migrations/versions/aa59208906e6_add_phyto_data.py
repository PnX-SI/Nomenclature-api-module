"""add phyto data

Revision ID: aa59208906e6
Revises: 78fffc4ef5ce
Create Date: 2025-08-27 18:31:33.767464

"""

import importlib.resources

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text


# revision identifiers, used by Alembic.
revision = "aa59208906e6"
down_revision = "78fffc4ef5ce"
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
            "pypnnomenclature.migrations.data", "nomenclatures_inpn_phyto_v3.sql"
        )
    )


def downgrade():
    #ToDo : Verify if the downgrade works
    delete_nomenclatures("STRATE_VEGETATION")
    delete_nomenclatures("PHYTO_ABUNDANCE")
