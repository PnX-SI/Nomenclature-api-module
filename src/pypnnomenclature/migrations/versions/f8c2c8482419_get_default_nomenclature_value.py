"""fix ref_nomenclatures.get_default_nomenclature_value

Revision ID: f8c2c8482419
Revises: 11e7741319fd
Create Date: 2021-10-06 10:45:42.264034

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f8c2c8482419"
down_revision = "11e7741319fd"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
    CREATE OR REPLACE FUNCTION ref_nomenclatures.get_default_nomenclature_value(mytype character varying, myidorganism integer DEFAULT NULL::integer)
     RETURNS integer
     LANGUAGE plpgsql
     IMMUTABLE
    AS $function$
    --Function that return the default nomenclature id with wanted nomenclature type (mnemonique), organism id
    --Return -1 if nothing matches with given parameters
      DECLARE
        thenomenclatureid integer;
      BEGIN
        SELECT
            INTO thenomenclatureid id_nomenclature,
            CASE 
                WHEN id_organisme = myidorganism THEN 1
                ELSE 0
            END priority
        FROM ref_nomenclatures.defaults_nomenclatures_value dnv
        JOIN utilisateurs.bib_organismes o
        ON o.id_organisme = dnv.id_organism 
        WHERE mnemonique_type = mytype
        AND (id_organisme = myidorganism OR id_organisme = NULL OR nom_organisme = 'ALL')
        ORDER BY priority DESC
        LIMIT 1;
        RETURN thenomenclatureid;
      END;
    $function$
    ;
    """
    )


def downgrade():
    op.execute(
        """
    CREATE OR REPLACE FUNCTION ref_nomenclatures.get_default_nomenclature_value(mytype character varying, myidorganism integer DEFAULT NULL)
     RETURNS integer
     LANGUAGE plpgsql
     IMMUTABLE
    AS $function$
    --Function that return the default nomenclature id with wanted nomenclature type (mnemonique), organism id
    --Return -1 if nothing matches with given parameters
      DECLARE
        thenomenclatureid integer;
      BEGIN
          SELECT INTO thenomenclatureid id_nomenclature
          FROM ref_nomenclatures.defaults_nomenclatures_value dnv
          JOIN utilisateurs.bib_organismes o
          ON o.id_organisme = dnv.id_organism
          WHERE mnemonique_type = mytype
          AND (dnv.id_organism = myidorganism OR (myidorganism IS NULL AND o.nom_organisme = 'ALL'))
          ORDER BY id_organism DESC LIMIT 1;
        IF (thenomenclatureid IS NOT NULL) THEN
          RETURN thenomenclatureid;
        END IF;
        RETURN -1;
      END;
    $function$
    ;
    """
    )
