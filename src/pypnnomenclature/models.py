from typing import Optional
import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.sql import select, func
from utils_flask_sqla.serializers import serializable

from pypnnomenclature.env import db


@serializable
class CorTaxrefNomenclature(db.Model):
    """
    Relation entre taxonomie et nomenclature.
    A n'utiliser uniquement lorsque que l'extension 'taxonomie' des nomenclatures est installée
    """

    __tablename__ = "cor_taxref_nomenclature"
    __table_args__ = {"schema": "ref_nomenclatures"}
    id_nomenclature: Mapped[int] = mapped_column(
        ForeignKey("ref_nomenclatures.t_nomenclatures.id_nomenclature"),
        primary_key=True,
    )
    regne: Mapped[str] = mapped_column(primary_key=True)
    group2_inpn: Mapped[str] = mapped_column(primary_key=True)
    group3_inpn: Mapped[str] = mapped_column(primary_key=True)


@serializable(
    exclude=[
        "label_en",
        "definition_en",
        "label_es",
        "definition_es",
        "label_de",
        "definition_de",
        "label_it",
        "definition_it",
        "meta_create_date",
        "meta_update_date",
    ]
)
class TNomenclatures(db.Model):
    __tablename__ = "t_nomenclatures"
    __table_args__ = {"schema": "ref_nomenclatures"}
    id_nomenclature: Mapped[int] = mapped_column(primary_key=True)
    id_type: Mapped[Optional[int]] = mapped_column(
        ForeignKey("ref_nomenclatures.bib_nomenclatures_types.id_type")
    )
    nomenclature_type: Mapped[Optional["BibNomenclaturesTypes"]] = relationship(
        "BibNomenclaturesTypes",
        backref="nomenclatures",
    )
    cd_nomenclature: Mapped[Optional[str]]
    mnemonique: Mapped[Optional[str]]
    label_default: Mapped[Optional[str]]
    definition_default: Mapped[Optional[str]]
    label_fr: Mapped[Optional[str]]
    definition_fr: Mapped[Optional[str]]
    label_en: Mapped[Optional[str]]
    definition_en: Mapped[Optional[str]]
    label_es: Mapped[Optional[str]]
    definition_es: Mapped[Optional[str]]
    label_de: Mapped[Optional[str]]
    definition_de: Mapped[Optional[str]]
    label_it: Mapped[Optional[str]]
    definition_it: Mapped[Optional[str]]
    source: Mapped[Optional[str]]
    statut: Mapped[Optional[str]]
    id_broader: Mapped[Optional[int]]
    hierarchy: Mapped[Optional[str]]
    active: Mapped[Optional[bool]]
    meta_create_date: Mapped[Optional[datetime.datetime]]
    meta_update_date: Mapped[Optional[datetime.datetime]]

    @staticmethod
    def get_default_nomenclature(mnemonique, id_organism=0):
        q = select(
            func.ref_nomenclatures.get_default_nomenclature_value(mnemonique, id_organism).label(
                "default"
            )
        )
        result = db.session.execute(q)
        return result.fetchone().default


class TNomenclatureTaxonomy(TNomenclatures):
    """
    Hérite de TNomenclatures, rajoute une relation vers CorTaxrefNomenclature
    """

    taxref: Mapped[list["CorTaxrefNomenclature"]] = relationship(
        "CorTaxrefNomenclature", lazy="joined"
    )


@serializable
class BibNomenclaturesTypes(db.Model):
    __tablename__ = "bib_nomenclatures_types"
    __table_args__ = {"schema": "ref_nomenclatures"}
    id_type: Mapped[int] = mapped_column(primary_key=True)
    mnemonique: Mapped[Optional[str]]
    label_default: Mapped[Optional[str]]
    definition_default: Mapped[Optional[str]]
    label_fr: Mapped[Optional[str]]
    definition_fr: Mapped[Optional[str]]
    label_en: Mapped[Optional[str]]
    definition_en: Mapped[Optional[str]]
    label_es: Mapped[Optional[str]]
    definition_es: Mapped[Optional[str]]
    label_de: Mapped[Optional[str]]
    definition_de: Mapped[Optional[str]]
    label_it: Mapped[Optional[str]]
    definition_it: Mapped[Optional[str]]
    source: Mapped[Optional[str]]
    statut: Mapped[Optional[str]]
    meta_create_date: Mapped[Optional[datetime.datetime]]
    meta_update_date: Mapped[Optional[datetime.datetime]]

    def __repr__(self):
        return self.label_default

    @staticmethod
    def get_default_nomenclature(mnemonique, id_organism=0):
        q = select(
            func.ref_nomenclatures.get_default_nomenclature_value(mnemonique, id_organism).label(
                "default"
            )
        )
        result = db.session.execute(q)
        return result.fetchone().default


class BibNomenclaturesTypeTaxo(BibNomenclaturesTypes):
    """
    Hérite de BibNomenclaturesTypes, rajoute simplement une relation vers 'nomenclature' avec la jointure vers la taxonomie
    """

    taxonomic_nomenclatures: Mapped[list["TNomenclatureTaxonomy"]] = relationship(
        "TNomenclatureTaxonomy",
        primaryjoin="and_(TNomenclatureTaxonomy.id_type == BibNomenclaturesTypes.id_type, TNomenclatureTaxonomy.active == True)",
        lazy="joined",
        order_by="TNomenclatureTaxonomy.hierarchy",
        viewonly=True,
    )


# Modèle utilisé seulement si l'extension 'taxonomie'
# du module est activée et installée
@serializable
class VNomenclatureTaxonomie(db.Model):
    __tablename__ = "v_nomenclature_taxonomie"
    __table_args__ = {"schema": "ref_nomenclatures"}
    id_type: Mapped[Optional[int]]
    type_label: Mapped[Optional[str]]
    type_definition: Mapped[Optional[str]]
    type_label_fr: Mapped[Optional[str]]
    type_definition_fr: Mapped[Optional[str]]
    type_label_en: Mapped[Optional[str]]
    type_definition_en: Mapped[Optional[str]]
    type_label_es: Mapped[Optional[str]]
    type_definition_es: Mapped[Optional[str]]
    type_label_de: Mapped[Optional[str]]
    type_definition_de: Mapped[Optional[str]]
    type_label_it: Mapped[Optional[str]]
    type_definition_it: Mapped[Optional[str]]
    regne: Mapped[str] = mapped_column(primary_key=True)
    group2_inpn: Mapped[str] = mapped_column(primary_key=True)
    group3_inpn: Mapped[str] = mapped_column(primary_key=True)
    id_nomenclature: Mapped[int] = mapped_column(primary_key=True)
    mnemonique: Mapped[Optional[str]]
    nomenclature_label: Mapped[Optional[str]]
    nomenclature_definition: Mapped[Optional[str]]
    nomenclature_label_fr: Mapped[Optional[str]]
    nomenclature_definition_fr: Mapped[Optional[str]]
    nomenclature_label_en: Mapped[Optional[str]]
    nomenclature_definition_en: Mapped[Optional[str]]
    nomenclature_label_es: Mapped[Optional[str]]
    nomenclature_definition_es: Mapped[Optional[str]]
    nomenclature_label_de: Mapped[Optional[str]]
    nomenclature_definition_de: Mapped[Optional[str]]
    nomenclature_label_it: Mapped[Optional[str]]
    nomenclature_definition_it: Mapped[Optional[str]]
    id_broader: Mapped[Optional[int]]
    hierarchy: Mapped[Optional[str]]
