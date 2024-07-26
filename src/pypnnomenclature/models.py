from importlib import import_module
from flask import current_app
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
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
    id_nomenclature = db.Column(
        db.Integer,
        ForeignKey("ref_nomenclatures.t_nomenclatures.id_nomenclature"),
        primary_key=True,
    )
    regne = db.Column(db.Unicode, primary_key=True)
    group2_inpn = db.Column(db.Unicode, primary_key=True)
    group3_inpn = db.Column(db.Unicode, primary_key=True)


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
    id_nomenclature = db.Column(db.Integer, primary_key=True)
    id_type = db.Column(
        db.Integer, ForeignKey("ref_nomenclatures.bib_nomenclatures_types.id_type")
    )
    nomenclature_type = relationship(
        "BibNomenclaturesTypes",
        backref="nomenclatures",
    )
    cd_nomenclature = db.Column(db.Unicode)
    mnemonique = db.Column(db.Unicode)
    label_default = db.Column(db.Unicode)
    definition_default = db.Column(db.Unicode)
    label_fr = db.Column(db.Unicode)
    definition_fr = db.Column(db.Unicode)
    label_en = db.Column(db.Unicode)
    definition_en = db.Column(db.Unicode)
    label_es = db.Column(db.Unicode)
    definition_es = db.Column(db.Unicode)
    label_de = db.Column(db.Unicode)
    definition_de = db.Column(db.Unicode)
    label_it = db.Column(db.Unicode)
    definition_it = db.Column(db.Unicode)
    source = db.Column(db.Unicode)
    statut = db.Column(db.Unicode)
    id_broader = db.Column(db.Integer)
    hierarchy = db.Column(db.Unicode)
    active = db.Column(db.BOOLEAN)
    meta_create_date = db.Column(db.DateTime)
    meta_update_date = db.Column(db.DateTime)

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

    taxref = relationship("CorTaxrefNomenclature", lazy="joined")


@serializable
class BibNomenclaturesTypes(db.Model):
    __tablename__ = "bib_nomenclatures_types"
    __table_args__ = {"schema": "ref_nomenclatures"}
    id_type = db.Column(db.Integer, primary_key=True)
    mnemonique = db.Column(db.Unicode)
    label_default = db.Column(db.Unicode)
    definition_default = db.Column(db.Unicode)
    label_fr = db.Column(db.Unicode)
    definition_fr = db.Column(db.Unicode)
    label_en = db.Column(db.Unicode)
    definition_en = db.Column(db.Unicode)
    label_es = db.Column(db.Unicode)
    definition_es = db.Column(db.Unicode)
    label_de = db.Column(db.Unicode)
    definition_de = db.Column(db.Unicode)
    label_it = db.Column(db.Unicode)
    definition_it = db.Column(db.Unicode)
    source = db.Column(db.Unicode)
    statut = db.Column(db.Unicode)
    meta_create_date = db.Column(db.DateTime)
    meta_update_date = db.Column(db.DateTime)

    def __repr__(self):
        return self.label_default

    @staticmethod
    def get_default_nomenclature(mnemonique, id_organism=0):
        q = select(
            [
                func.ref_nomenclatures.get_default_nomenclature_value(
                    mnemonique, id_organism
                ).label("default")
            ]
        )
        result = db.session.execute(q)
        return result.fetchone().default


class BibNomenclaturesTypeTaxo(BibNomenclaturesTypes):
    """
    Hérite de BibNomenclaturesTypes, rajoute simplement une relation vers 'nomenclature' avec la jointure vers la taxonomie
    """

    taxonomic_nomenclatures = relationship(
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
    id_type = db.Column(db.Integer)
    type_label = db.Column(db.Unicode)
    type_definition = db.Column(db.Unicode)
    type_label_fr = db.Column(db.Unicode)
    type_definition_fr = db.Column(db.Unicode)
    type_label_en = db.Column(db.Unicode)
    type_definition_en = db.Column(db.Unicode)
    type_label_es = db.Column(db.Unicode)
    type_definition_es = db.Column(db.Unicode)
    type_label_de = db.Column(db.Unicode)
    type_definition_de = db.Column(db.Unicode)
    type_label_it = db.Column(db.Unicode)
    type_definition_it = db.Column(db.Unicode)
    regne = db.Column(db.Unicode, primary_key=True)
    group2_inpn = db.Column(db.Unicode, primary_key=True)
    group3_inpn = db.Column(db.Unicode, primary_key=True)
    id_nomenclature = db.Column(db.Integer, primary_key=True)
    mnemonique = db.Column(db.Unicode)
    nomenclature_label = db.Column(db.Unicode)
    nomenclature_definition = db.Column(db.Unicode)
    nomenclature_label_fr = db.Column(db.Unicode)
    nomenclature_definition_fr = db.Column(db.Unicode)
    nomenclature_label_en = db.Column(db.Unicode)
    nomenclature_definition_en = db.Column(db.Unicode)
    nomenclature_label_es = db.Column(db.Unicode)
    nomenclature_definition_es = db.Column(db.Unicode)
    nomenclature_label_de = db.Column(db.Unicode)
    nomenclature_definition_de = db.Column(db.Unicode)
    nomenclature_label_it = db.Column(db.Unicode)
    nomenclature_definition_it = db.Column(db.Unicode)
    id_broader = db.Column(db.Integer)
    hierarchy = db.Column(db.Unicode)
