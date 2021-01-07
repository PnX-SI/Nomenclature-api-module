"""Complete ref_nomenclature schema with taxonomie

Revision ID: 6ddded935869
Revises: 92fc0589d33a
Create Date: 2020-12-31 01:06:26.215026

"""
from alembic import op, context
import sqlalchemy as sa
import pkg_resources
from distutils.util import strtobool


# revision identifiers, used by Alembic.
revision = '6ddded935869'
down_revision = '92fc0589d33a'
branch_labels = []
depends_on = (
    'c59c225e1c42',  # taxonomie schema with inpn data
)

schema = 'ref_nomenclatures'


def upgrade():
    operations = pkg_resources.resource_string("pypnnomenclature.migrations",
                                               "data/nomenclatures_taxonomie.sql").decode('utf-8')
    op.execute(operations)
    if strtobool(context.get_x_argument(as_dictionary=True).get('nomenclatures-taxonomie-data', "true")):
        operations = pkg_resources.resource_string("pypnnomenclature.migrations", "data/nomenclatures_taxonomie_data.sql").decode('utf-8')
        op.execute(operations)


def downgrade():
    op.execute(f"DROP TRIGGER tri_meta_dates_change_cor_taxref_sensitivity ON {schema}.cor_taxref_sensitivity")
    op.execute(f"DROP TRIGGER tri_meta_dates_change_cor_taxref_nomenclature ON {schema}.cor_taxref_nomenclature")
    for view in [
                'v_nomenclature_taxonomie',
                'v_technique_obs',
                'v_eta_bio',
                'v_stade_vie',
                'v_sexe',
                'v_objet_denbr',
                'v_type_denbr',
                'v_meth_obs',
                'v_statut_bio',
                'v_naturalite',
                'v_preuve_exist',
                'v_statut_obs',
                'v_statut_valid',
                'v_niv_precis',
                'v_resource_typ',
                'v_data_typ',
                'v_sampling_plan_typ',
                'v_sampling_units_typ',
                'v_meth_determin',
            ][::-1]:
        op.execute(f"DROP VIEW {schema}.{view}")
    op.drop_table('cor_taxref_sensitivity', schema=schema)
    op.drop_table('cor_taxref_nomenclature', schema=schema)
    for function in ['calculate_sensitivity', 'get_filtered_nomenclature']:
        op.execute(f"DROP FUNCTION {schema}.{function}")
