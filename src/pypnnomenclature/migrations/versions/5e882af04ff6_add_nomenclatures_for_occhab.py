"""add_nomenclatures_for_occhab

Revision ID: 5e882af04ff6
Revises: ee1146f6c0f4
Create Date: 2024-07-18 14:38:21.143524

"""

from alembic import op
from pypnnomenclature.models import BibNomenclaturesTypes, TNomenclatures
import sqlalchemy as sa
from sqlalchemy.orm.session import Session


# revision identifiers, used by Alembic.
revision = "5e882af04ff6"
down_revision = "ee1146f6c0f4"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        sa.insert(BibNomenclaturesTypes).values(
            dict(
                mnemonique="MOSAIQUE_HAB",
                label_fr=" MosaiqueValue",
                label_default=" MosaiqueValue",
                definition_fr="Type de mosaïque d'habitats.",
                source="SINP",
                statut="Validé",
            )
        )
    )

    nomenclatures = [
        dict(
            id_type=sa.func.ref_nomenclatures.get_id_nomenclature_type("MOSAIQUE_HAB"),
            cd_nomenclature="1",
            mnemonique="Mosaïque spatiale",
            label_fr="Mosaïque spatiale",
            definition_fr="""Deux habitats (ou plus) s’interpénètrent de façon homogène ou un habitat est
dispersé au sein d’un habitat « dominant », et ces habitats ne présentent pas de liens dynamiques mais des
liens topographiques induisant des variations édaphiques""",
            source="SINP",
            statut="Validé",
            id_broader=0,
            hierarchy=None,
            active=True,
            label_default="Mosaïque spatiale",
        ),
        dict(
            id_type=sa.func.ref_nomenclatures.get_id_nomenclature_type("MOSAIQUE_HAB"),
            cd_nomenclature="2",
            mnemonique="Mosaïque temporelle",
            label_fr="Mosaïque temporelle",
            definition_fr="""Les habitats imbriqués présentent des liens dynamiques et la limite entre
deux habitats ne peut être tracée de façon exacte en raison du gradient ou du continuum existant.""",
            source="SINP",
            statut="Validé",
            id_broader=0,
            hierarchy=None,
            active=True,
            label_default="Mosaïque temporelle",
        ),
        dict(
            id_type=sa.func.ref_nomenclatures.get_id_nomenclature_type("MOSAIQUE_HAB"),
            cd_nomenclature="3",
            mnemonique="Mosaïque mixte",
            label_fr="Mosaïque mixte",
            definition_fr="""Les habitats imbriqués présentent à la fois des liens topographiques (mosaïque
spatiale) et des liens dynamiques (mosaïque temporelle).""",
            source="SINP",
            statut="Validé",
            id_broader=0,
            hierarchy=None,
            active=True,
            label_default="Mosaïque mixte",
        ),
        dict(
            id_type=sa.func.ref_nomenclatures.get_id_nomenclature_type("MOSAIQUE_HAB"),
            cd_nomenclature="4",
            mnemonique="Mosaïque de type inconnu",
            label_fr="Mosaïque de type inconnu",
            definition_fr="""Le type de mosaïque n'a pas été identifié ou la mosaïque d’habitats ne
peut être facilement rattachée à aucune des catégories citées précédemment.""",
            source="SINP",
            statut="Validé",
            id_broader=0,
            hierarchy=None,
            active=True,
            label_default="Mosaïque de type inconnu",
        ),
    ]
    for nom in nomenclatures:
        op.execute(sa.insert(TNomenclatures).values(**nom))


def downgrade():
    session = Session(bind=op.get_bind())
    id_nomenclature_type = session.scalar(
        sa.select(sa.func.ref_nomenclatures.get_id_nomenclature_type("MOSAIQUE_HAB"))
    )
    session.close()
    op.execute(
        sa.delete(TNomenclatures).where(
            TNomenclatures.id_type == id_nomenclature_type,
        ),
    )
    op.execute(
        sa.delete(BibNomenclaturesTypes).where(BibNomenclaturesTypes.mnemonique == "MOSAIQUE_HAB")
    )
