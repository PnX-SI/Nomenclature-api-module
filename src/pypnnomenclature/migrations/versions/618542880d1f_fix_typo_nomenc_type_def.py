"""fix typo in nomenclature type definition

Revision ID: 618542880d1f
Revises: a763fb554ff2
Create Date: 2022-07-28 14:43:31.883082

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "618542880d1f"
down_revision = "96a713739fdd"
branch_labels = None
depends_on = None


def copy_definition_fr_in_definition_default():
    op.execute(
        """
    UPDATE
        ref_nomenclatures.bib_nomenclatures_types
    SET
        definition_default = definition_fr
    WHERE
        mnemonique = 'OCC_COMPORTEMENT'
    """
    )


def upgrade():
    op.execute(
        """
    UPDATE
        ref_nomenclatures.bib_nomenclatures_types
    SET
        definition_fr = 'Nomenclature des comportements des occurrences observées'
    WHERE
        mnemonique = 'OCC_COMPORTEMENT'
    """
    )
    copy_definition_fr_in_definition_default()


def downgrade():
    op.execute(
        """
    UPDATE
        ref_nomenclatures.bib_nomenclatures_types
    SET
        definition_fr = 'Nomenclature des domportement des occurrences observées'
    WHERE
        mnemonique = 'OCC_COMPORTEMENT'
    """
    )
    copy_definition_fr_in_definition_default()
