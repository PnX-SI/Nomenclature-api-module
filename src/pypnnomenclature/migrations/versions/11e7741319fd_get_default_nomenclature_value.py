"""fix ref_nomenclatures.get_default_nomenclature_value

Revision ID: 11e7741319fd
Revises: 6015397d686a
Create Date: 2021-10-04 17:51:48.491261

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "11e7741319fd"
down_revision = "6015397d686a"
branch_labels = None
depends_on = None


def upgrade():
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


def downgrade():
    op.execute(
        """
    CREATE OR REPLACE FUNCTION ref_nomenclatures.get_default_nomenclature_value(mytype character varying, myidorganism integer DEFAULT 0)
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
          FROM ref_nomenclatures.defaults_nomenclatures_value
          WHERE mnemonique_type = mytype
          AND (id_organism = myidorganism OR id_organism = 0)
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
