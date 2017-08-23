
# coding: utf8
from __future__ import (unicode_literals, print_function,
                        absolute_import, division)

from flask_sqlalchemy import SQLAlchemy
from .utils import serializableModel

db = SQLAlchemy()

class TNomenclatures(serializableModel, db.Model):
    __tablename__ = 't_nomenclatures'
    __table_args__ = {'schema':'nomenclatures'}
    id_nomenclature = db.Column(db.Integer, primary_key=True)
    id_type =  db.Column(db.Integer)
    mnemonique = db.Column(db.Unicode)
    label_fr = db.Column(db.Unicode)
    definition_fr = db.Column(db.Unicode)
    source = db.Column(db.Unicode)
    statut = db.Column(db.Unicode)
    id_broader = db.Column(db.Integer)
    hierarchy = db.Column(db.Unicode)
    active = db.Column(db.BOOLEAN)
    meta_create_date = db.Column(db.DateTime)
    meta_update_date = db.Column(db.DateTime)


class BibNomenclaturesTypes(serializableModel, db.Model):
    __tablename__ = 'bib_nomenclatures_types'
    __table_args__ = {'schema':'nomenclatures'}
    id_type = db.Column(db.Integer, primary_key=True)
    mnemonique = db.Column(db.Unicode)
    label_fr = db.Column(db.Unicode)
    definition_fr = db.Column(db.Unicode)
    source = db.Column(db.Unicode)
    statut = db.Column(db.Unicode)
    meta_create_date = db.Column(db.DateTime)
    meta_update_date = db.Column(db.DateTime)



class VNomenclatureTaxonomie(serializableModel, db.Model):
    __tablename__ = 'v_nomenclature_taxonomie'
    __table_args__ = {'schema':'nomenclatures'}
    id_type = db.Column(db.Integer)
    type_nomenclature_label_fr = db.Column(db.Unicode)
    type_nomenclature_definition_fr = db.Column(db.Unicode)
    regne = db.Column(db.Unicode, primary_key=True)
    group2_inpn = db.Column(db.Unicode, primary_key=True)
    id_nomenclature = db.Column(db.Integer, primary_key=True)
    mnemonique = db.Column(db.Unicode)
    nomenclature_label_fr = db.Column(db.Unicode)
    nomenclature_definition_fr = db.Column(db.Unicode)
    id_broader = db.Column(db.Integer)
    hierarchy = db.Column(db.Unicode)
