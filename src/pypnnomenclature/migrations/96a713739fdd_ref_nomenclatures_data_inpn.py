''' nomenclatures insert data inpn

Revision ID: 96a713739fdd
Revises:
Create Date: 2021-09-16 15:36:57.784074
'''
import importlib.resources

from alembic import op, context
import sqlalchemy as sa
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision = '96a713739fdd'
down_revision = None
branch_labels = ('nomenclatures_data_inpn',)
depends_on = ('ref_nomenclatures')

MYDEFAULTLANGUAGE = context.get_x_argument(as_dictionary=True).get('MYDEFAULTLANGUAGE', 'fr')


def upgrade():
    operations = importlib.resources.read_text('pypnnomenclature.migrations.data', 'data_nomenclatures.sql').replace(':MYDEFAULTLANGUAGE', MYDEFAULTLANGUAGE)
    op.execute(operations)

# On supprime toutes les données de source SINP
def downgrade():
    op.execute('''
    DELETE FROM ref_nomenclatures.t_nomenclatures WHERE source = 'SINP';
    DELETE FROM ref_nomenclatures.bib_nomenclatures_type WHERE source = 'SINP';
    ''')

