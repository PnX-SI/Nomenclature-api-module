"""add_etat_conservation_hab

Revision ID: b19f75d0e9a3
Revises: 8eb9a12db289
Create Date: 2026-09-22 00:00:00.000000

"""

from alembic import op
from pypnnomenclature.models import BibNomenclaturesTypes, TNomenclatures
import sqlalchemy as sa
from sqlalchemy.orm.session import Session

# revision identifiers, used by Alembic.
revision = "b19f75d0e9a3"
down_revision = "8eb9a12db289"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        sa.insert(BibNomenclaturesTypes).values(
            dict(
                mnemonique="ETAT_CONSERVATION_HAB",
                label_fr="Etat de conservation de l'habitat",
                label_default="Etat de conservation de l'habitat",
                definition_fr="Etat de conservation d'un habitat observé.",
                source="SINP",
                statut="Validé",
            )
        )
    )

    nomenclatures = [
        dict(
            id_type=sa.func.ref_nomenclatures.get_id_nomenclature_type("ETAT_CONSERVATION_HAB"),
            cd_nomenclature="1",
            mnemonique="Optimal",
            label_fr="Optimal",
            definition_fr="",
            source="SINP",
            statut="Validé",
            id_broader=0,
            hierarchy=None,
            active=True,
            label_default="Optimal",
        ),
        dict(
            id_type=sa.func.ref_nomenclatures.get_id_nomenclature_type("ETAT_CONSERVATION_HAB"),
            cd_nomenclature="2",
            mnemonique="Favorable",
            label_fr="Favorable",
            definition_fr="",
            source="SINP",
            statut="Validé",
            id_broader=0,
            hierarchy=None,
            active=True,
            label_default="Favorable",
        ),
        dict(
            id_type=sa.func.ref_nomenclatures.get_id_nomenclature_type("ETAT_CONSERVATION_HAB"),
            cd_nomenclature="3",
            mnemonique="Altéré",
            label_fr="Altéré",
            definition_fr="",
            source="SINP",
            statut="Validé",
            id_broader=0,
            hierarchy=None,
            active=True,
            label_default="Altéré",
        ),
        dict(
            id_type=sa.func.ref_nomenclatures.get_id_nomenclature_type("ETAT_CONSERVATION_HAB"),
            cd_nomenclature="4",
            mnemonique="Dégradé",
            label_fr="Dégradé",
            definition_fr="",
            source="SINP",
            statut="Validé",
            id_broader=0,
            hierarchy=None,
            active=True,
            label_default="Dégradé",
        ),
    ]
    for nom in nomenclatures:
        op.execute(sa.insert(TNomenclatures).values(**nom))


def downgrade():
    session = Session(bind=op.get_bind())
    id_nomenclature_type = session.scalar(
        sa.select(sa.func.ref_nomenclatures.get_id_nomenclature_type("ETAT_CONSERVATION_HAB"))
    )
    session.close()
    op.execute(
        sa.delete(TNomenclatures).where(
            TNomenclatures.id_type == id_nomenclature_type,
        ),
    )
    op.execute(
        sa.delete(BibNomenclaturesTypes).where(
            BibNomenclaturesTypes.mnemonique == "ETAT_CONSERVATION_HAB"
        )
    )
