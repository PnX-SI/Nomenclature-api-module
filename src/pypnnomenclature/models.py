
# coding: utf8
from __future__ import (unicode_literals, print_function,
                        absolute_import, division)

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

from .utils import serializableModel

db = SQLAlchemy()


class TNomenclatures(serializableModel, db.Model):
    __tablename__ = 't_nomenclatures'
    __table_args__ = {'schema': 'ref_nomenclatures'}
    id_nomenclature = db.Column(db.Integer, primary_key=True)
    id_type = db.Column(
        db.Integer,
        ForeignKey('ref_nomenclatures.BibNomenclaturesTypes.id_type')
    )
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


class BibNomenclaturesTypes(serializableModel, db.Model):
    __tablename__ = 'bib_nomenclatures_types'
    __table_args__ = {'schema': 'ref_nomenclatures'}
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


class VNomenclatureTaxonomie(serializableModel, db.Model):
    __tablename__ = 'v_nomenclature_taxonomie'
    __table_args__ = {'schema': 'ref_nomenclatures'}
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
