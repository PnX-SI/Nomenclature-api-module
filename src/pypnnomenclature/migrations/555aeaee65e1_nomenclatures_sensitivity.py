"""nomenclatures_sensitivity

Revision ID: 555aeaee65e1
Revises:
Create Date: 2021-09-17 11:08:57.784074

"""
import importlib.resources

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '555aeaee65e1'
down_revision = None
branch_labels = ('nomenclatures_sensibility',)
depends_on = ('ref_nomenclatures', 'taxonomie')


def upgrade():
    op.execute(importlib.resources.read_text('pypnnomenclature.migrations.data', 'nomenclatures_sensitivity.sql'))


def downgrade():
    op.execute('''
    DROP TABLE ref_nomenclatures.cor_taxref_sensitivity;
    DROP FUNCTION FUNCTION ref_nomenclatures.calculate_sensitivity(integer, integer);
    ''')
