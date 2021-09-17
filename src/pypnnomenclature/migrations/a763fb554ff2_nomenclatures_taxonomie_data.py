'''nomenclatures_taxonomie insert data

Revision ID: a763fb554ff2
Revises:
Create Date: 2021-09-16 15:36:57.784074
'''
import importlib.resources

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a763fb554ff2'
down_revision = None
branch_labels = ('nomenclatures_taxonomie_data',)
depends_on = ('nomenclatures_data_inpn', 'nomenclatures_taxonomie')


def upgrade():
    op.execute(importlib.resources.read_text('pypnnomenclature.migrations.data', 'data_nomenclatures_taxonomie.sql'))

# On supprime toutes les données de source SINP
def downgrade():
    op.execute('''
    DELETE FROM ref_nomenclatures.cor_taxref_nomenclature;
    ''')

