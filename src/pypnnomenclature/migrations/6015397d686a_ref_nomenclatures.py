"""nomenclature schema 1.3.9

Revision ID: 6015397d686a
Revises:
Create Date: 2021-09-16 14:15:57.784074

"""
import importlib.resources

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6015397d686a'
down_revision = None
branch_labels = ('ref_nomenclatures',)
depends_on = ('sql_utils') # de utils_flask_sqla pour les fonctions de date dans le schema public

def upgrade():
    op.execute(importlib.resources.read_text('pypnnomenclature.migrations.data', 'nomenclatures.sql'))


def downgrade():
    op.execute("DROP SCHEMA ref_nomenclatures CASCADE")
