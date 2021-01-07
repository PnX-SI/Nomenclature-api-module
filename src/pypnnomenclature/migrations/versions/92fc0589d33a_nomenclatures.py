"""Create ref_nomenclatures schema

Revision ID: 92fc0589d33a
Revises: 
Create Date: 2020-12-28 13:03:51.529053

"""
from alembic import op, context
import sqlalchemy as sa
import pkg_resources
from distutils.util import strtobool


# revision identifiers, used by Alembic.
revision = '92fc0589d33a'
down_revision = None
branch_labels = ('ref_nomenclatures',)
depends_on = (
        '081ddfc0abb4',  # public functions
        'utilisateurs',
)

schema = 'ref_nomenclatures'


def upgrade():
    operations = pkg_resources.resource_string("pypnnomenclature.migrations",
                                               "data/nomenclatures.sql").decode('utf-8')
    op.execute(operations)
    if strtobool(context.get_x_argument(as_dictionary=True).get('nomenclatures-data', "true")):
        defaultlanguage = context.get_x_argument(as_dictionary=True).get('defaultlanguage', 'fr')
        operations = pkg_resources.resource_string("pypnnomenclature.migrations", "data/nomenclatures_data.sql").decode('utf-8')
        operations = operations.replace('DEFAULTLANGUAGE', defaultlanguage)
        op.execute(operations)


def downgrade():
    op.execute(f"DROP TRIGGER tri_meta_dates_change_t_nomenclatures ON {schema}.t_nomenclatures")
    op.execute(f"DROP TRIGGER tri_meta_dates_change_bib_nomenclatures_types ON {schema}.bib_nomenclatures_types")
    op.execute(f"DROP INDEX {schema}.index_t_nomenclatures_bib_nomenclatures_types_fkey")
    for table in [
                'cor_application_nomenclature',
                'defaults_nomenclatures_value',
                'cor_nomenclatures_relations',
                't_nomenclatures',
                'bib_nomenclatures_types',
            ]:
        op.drop_table(table, schema=schema)
    for function in [
                'get_nomenclature_label_by_cdnom_mnemonique',
                'get_nomenclature_label_by_cdnom_mnemonique_and_language',
                'get_cd_nomenclature',
                'get_nomenclature_label',
                'get_id_nomenclature',
                'check_nomenclature_type_by_id',
                'check_nomenclature_type_by_cd_nomenclature',
                'check_nomenclature_type_by_mnemonique',
                'get_default_nomenclature_value',
                'get_id_nomenclature_type',
            ]:
        op.execute(f"DROP FUNCTION {schema}.{function}")
    op.execute(f"DROP SCHEMA {schema}")
