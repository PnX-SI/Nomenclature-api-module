"""fix ref_nomenclatures.get_nomenclature_label

Revision ID: b820c66d8daa
Revises: f8c2c8482419
Create Date: 2021-12-10 10:07:09.478526

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b820c66d8daa"
down_revision = "f8c2c8482419"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE OR REPLACE FUNCTION ref_nomenclatures.get_nomenclature_label(
            myidnomenclature integer DEFAULT NULL::integer,
            mylanguage character varying DEFAULT 'fr'::character varying)
        RETURNS character varying
        LANGUAGE plpgsql
        IMMUTABLE
        AS $function$
        --Function which return the label from the id_nomenclature and the language
        DECLARE
            labelfield character varying;
            thelabel character varying;
        BEGIN
        IF myidnomenclature IS NULL THEN
            RETURN NULL;
        END IF;

        labelfield = 'label_'||mylanguage;
        EXECUTE format('
            SELECT  %s
            FROM ref_nomenclatures.t_nomenclatures n
            WHERE id_nomenclature = %s
        ',labelfield, myidnomenclature
        )
        INTO thelabel;
        return thelabel;
        END;
        $function$
        ;
    """
    )


def downgrade():
    op.execute(
        """
        CREATE OR REPLACE FUNCTION ref_nomenclatures.get_nomenclature_label(
            myidnomenclature integer DEFAULT NULL::integer,
            mylanguage character varying DEFAULT 'fr'::character varying)
        RETURNS character varying
        LANGUAGE plpgsql
        IMMUTABLE
        AS $function$
        --Function which return the label from the id_nomenclature and the language
        DECLARE
            labelfield character varying;
            thelabel character varying;
        BEGIN
        labelfield = 'label_'||mylanguage;
        EXECUTE format( ' SELECT  %s
        FROM ref_nomenclatures.t_nomenclatures n
        WHERE id_nomenclature = %s',labelfield, myidnomenclature ) INTO thelabel;
        return thelabel;
        END;
        $function$
        ;
    """
    )
