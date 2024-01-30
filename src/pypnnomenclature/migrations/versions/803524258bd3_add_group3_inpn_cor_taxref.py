"""add group3_inpn cor_taxref_nomenclature

Revision ID: 803524258bd3
Revises: f5436084bf17
Create Date: 2023-09-04 07:57:35.371378

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "803524258bd3"
down_revision = "f5436084bf17"
branch_labels = None
depends_on = "33e20a7682b4"


def upgrade():
    op.add_column(
        table_name="cor_taxref_nomenclature",
        column=sa.Column("group3_inpn", sa.VARCHAR(255), server_default="all"),
        schema="ref_nomenclatures",
    )
    op.execute(
        """ALTER TABLE ref_nomenclatures.cor_taxref_nomenclature 
               ADD CONSTRAINT check_cor_taxref_nomenclature_isgroup3inpn 
               CHECK ((taxonomie.check_is_group3inpn((group3_inpn)::text) OR ((group3_inpn)::text = 'all'::text))) NOT VALID   
        """
    )
    with op.batch_alter_table(
        table_name="cor_taxref_nomenclature", schema="ref_nomenclatures"
    ) as batch:
        batch.drop_constraint("pk_cor_taxref_nomenclature")
        batch.create_primary_key(
            constraint_name="pk_cor_taxref_nomenclature",
            columns=["id_nomenclature", "regne", "group2_inpn", "group3_inpn"],
        )
    op.execute("DROP VIEW ref_nomenclatures.v_nomenclature_taxonomie")
    op.execute(
        """
CREATE OR REPLACE VIEW ref_nomenclatures.v_nomenclature_taxonomie
AS SELECT tn.id_type,
    tn.label_default AS type_label,
    tn.definition_default AS type_definition,
    tn.label_fr AS type_label_fr,
    tn.definition_fr AS type_definition_fr,
    tn.label_en AS type_label_en,
    tn.definition_en AS type_definition_en,
    tn.label_es AS type_label_es,
    tn.definition_es AS type_definition_es,
    tn.label_de AS type_label_de,
    tn.definition_de AS type_definition_de,
    tn.label_it AS type_label_it,
    tn.definition_it AS type_definition_it,
    ctn.regne,
    ctn.group2_inpn,
    ctn.group3_inpn,
    n.id_nomenclature,
    n.mnemonique,
    n.label_default AS nomenclature_label,
    n.definition_default AS nomenclature_definition,
    n.label_fr AS nomenclature_label_fr,
    n.definition_fr AS nomenclature_definition_fr,
    n.label_en AS nomenclature_label_en,
    n.definition_en AS nomenclature_definition_en,
    n.label_es AS nomenclature_label_es,
    n.definition_es AS nomenclature_definition_es,
    n.label_de AS nomenclature_label_de,
    n.definition_de AS nomenclature_definition_de,
    n.label_it AS nomenclature_label_it,
    n.definition_it AS nomenclature_definition_it,
    n.id_broader,
    n.hierarchy
   FROM ref_nomenclatures.t_nomenclatures n
     JOIN ref_nomenclatures.bib_nomenclatures_types tn ON tn.id_type = n.id_type
     JOIN ref_nomenclatures.cor_taxref_nomenclature ctn ON ctn.id_nomenclature = n.id_nomenclature
  WHERE n.active = true
  ORDER BY tn.id_type, ctn.regne, ctn.group2_inpn, n.id_nomenclature;
        """
    )


def downgrade():
    with op.batch_alter_table(
        table_name="cor_taxref_nomenclature", schema="ref_nomenclatures"
    ) as batch:
        batch.drop_constraint("check_cor_taxref_nomenclature_isgroup3inpn")
        batch.drop_constraint("pk_cor_taxref_nomenclature")
        batch.create_primary_key(
            constraint_name="pk_cor_taxref_nomenclature",
            columns=["id_nomenclature", "regne", "group2_inpn"],
        )
    op.execute("DROP VIEW ref_nomenclatures.v_nomenclature_taxonomie")
    op.drop_column("cor_taxref_nomenclature", "group3_inpn", schema="ref_nomenclatures")
    op.execute(
        """
               CREATE VIEW ref_nomenclatures.v_nomenclature_taxonomie
AS SELECT tn.id_type,
    tn.label_default AS type_label,
    tn.definition_default AS type_definition,
    tn.label_fr AS type_label_fr,
    tn.definition_fr AS type_definition_fr,
    tn.label_en AS type_label_en,
    tn.definition_en AS type_definition_en,
    tn.label_es AS type_label_es,
    tn.definition_es AS type_definition_es,
    tn.label_de AS type_label_de,
    tn.definition_de AS type_definition_de,
    tn.label_it AS type_label_it,
    tn.definition_it AS type_definition_it,
    ctn.regne,
    ctn.group2_inpn,
    n.id_nomenclature,
    n.mnemonique,
    n.label_default AS nomenclature_label,
    n.definition_default AS nomenclature_definition,
    n.label_fr AS nomenclature_label_fr,
    n.definition_fr AS nomenclature_definition_fr,
    n.label_en AS nomenclature_label_en,
    n.definition_en AS nomenclature_definition_en,
    n.label_es AS nomenclature_label_es,
    n.definition_es AS nomenclature_definition_es,
    n.label_de AS nomenclature_label_de,
    n.definition_de AS nomenclature_definition_de,
    n.label_it AS nomenclature_label_it,
    n.definition_it AS nomenclature_definition_it,
    n.id_broader,
    n.hierarchy
   FROM ref_nomenclatures.t_nomenclatures n
     JOIN ref_nomenclatures.bib_nomenclatures_types tn ON tn.id_type = n.id_type
     JOIN ref_nomenclatures.cor_taxref_nomenclature ctn ON ctn.id_nomenclature = n.id_nomenclature
  WHERE n.active = true
  ORDER BY tn.id_type, ctn.regne, ctn.group2_inpn, n.id_nomenclature;"""
    )
