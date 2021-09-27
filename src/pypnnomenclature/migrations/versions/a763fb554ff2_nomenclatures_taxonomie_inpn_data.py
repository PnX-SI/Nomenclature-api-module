'''insert taxonomic inpn data in ref_nomenclatures

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
branch_labels = ('nomenclatures_taxonomie_inpn_data',)
depends_on = (
    'f5436084bf17',  # nomenclatures_taxonomie
    '96a713739fdd',  # nomenclatures_inpn_data
    'f61f95136ec3',  # taxonomie_inpn_data
)


def upgrade():
    op.execute(importlib.resources.read_text('pypnnomenclature.migrations.data', 'nomenclatures_taxonomie_inpn_data.sql'))

def downgrade():
    # WARNING: we do not check cor_taxref_nomenclature contains only INPN data…
    # If you are not sure, delete unwanted data manually and then stamp previous revision.
    op.execute("TRUNCATE TABLE ref_nomenclatures.cor_taxref_nomenclature")

