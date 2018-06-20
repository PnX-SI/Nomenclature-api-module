
# coding: utf8
from __future__ import (unicode_literals, print_function,
                        absolute_import, division)

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import select, func
from .utils import serializableModel

from .env import DB

class BibNomenclaturesTypes(serializableModel, DB.Model):
    __tablename__ = 'bib_nomenclatures_types'
    __table_args__ = {'schema': 'ref_nomenclatures'}
    id_type = DB.Column(DB.Integer, primary_key=True)
    mnemonique = DB.Column(DB.Unicode)
    label_default = DB.Column(DB.Unicode)
    definition_default = DB.Column(DB.Unicode)
    label_fr = DB.Column(DB.Unicode)
    definition_fr = DB.Column(DB.Unicode)
    label_en = DB.Column(DB.Unicode)
    definition_en = DB.Column(DB.Unicode)
    label_es = DB.Column(DB.Unicode)
    definition_es = DB.Column(DB.Unicode)
    label_de = DB.Column(DB.Unicode)
    definition_de = DB.Column(DB.Unicode)
    label_it = DB.Column(DB.Unicode)
    definition_it = DB.Column(DB.Unicode)
    source = DB.Column(DB.Unicode)
    statut = DB.Column(DB.Unicode)
    meta_create_date = DB.Column(DB.DateTime)
    meta_update_date = DB.Column(DB.DateTime)
    nomenclature_items = relationship("TNomenclatures")

    def __repr__(self):
        return self.label_default

class TNomenclatures(serializableModel, DB.Model):
    __tablename__ = 't_nomenclatures'
    __table_args__ = {'schema': 'ref_nomenclatures'}
    id_nomenclature = DB.Column(DB.Integer, primary_key=True)
    id_type = DB.Column(
        DB.Integer,
        ForeignKey('ref_nomenclatures.bib_nomenclatures_types.id_type')
    )
    cd_nomenclature = DB.Column(DB.Unicode)
    mnemonique = DB.Column(DB.Unicode)
    label_default = DB.Column(DB.Unicode)
    definition_default = DB.Column(DB.Unicode)
    label_fr = DB.Column(DB.Unicode)
    definition_fr = DB.Column(DB.Unicode)
    label_en = DB.Column(DB.Unicode)
    definition_en = DB.Column(DB.Unicode)
    label_es = DB.Column(DB.Unicode)
    definition_es = DB.Column(DB.Unicode)
    label_de = DB.Column(DB.Unicode)
    definition_de = DB.Column(DB.Unicode)
    label_it = DB.Column(DB.Unicode)
    definition_it = DB.Column(DB.Unicode)
    source = DB.Column(DB.Unicode)
    statut = DB.Column(DB.Unicode)
    id_broader = DB.Column(DB.Integer)
    hierarchy = DB.Column(DB.Unicode)
    active = DB.Column(DB.BOOLEAN)
    meta_create_date = DB.Column(DB.DateTime)
    meta_update_date = DB.Column(DB.DateTime)
    nomenclature_type_name = relationship("BibNomenclaturesTypes", back_populates="nomenclature_items")


    @staticmethod
    def get_default_nomenclature(id_type, id_organism=0):
        q = select([func.ref_nomenclatures.get_default_nomenclature_value(id_type, id_organism).label('default')])
        result = DB.session.execute(q)
        return result.fetchone()['default']



class VNomenclatureTaxonomie(serializableModel, DB.Model):
    __tablename__ = 'v_nomenclature_taxonomie'
    __table_args__ = {'schema': 'ref_nomenclatures'}
    id_type = DB.Column(DB.Integer)
    type_label = DB.Column(DB.Unicode)
    type_definition = DB.Column(DB.Unicode)
    type_label_fr = DB.Column(DB.Unicode)
    type_definition_fr = DB.Column(DB.Unicode)
    type_label_en = DB.Column(DB.Unicode)
    type_definition_en = DB.Column(DB.Unicode)
    type_label_es = DB.Column(DB.Unicode)
    type_definition_es = DB.Column(DB.Unicode)
    type_label_de = DB.Column(DB.Unicode)
    type_definition_de = DB.Column(DB.Unicode)
    type_label_it = DB.Column(DB.Unicode)
    type_definition_it = DB.Column(DB.Unicode)
    regne = DB.Column(DB.Unicode, primary_key=True)
    group2_inpn = DB.Column(DB.Unicode, primary_key=True)
    id_nomenclature = DB.Column(DB.Integer, primary_key=True)
    mnemonique = DB.Column(DB.Unicode)
    nomenclature_label = DB.Column(DB.Unicode)
    nomenclature_definition = DB.Column(DB.Unicode)
    nomenclature_label_fr = DB.Column(DB.Unicode)
    nomenclature_definition_fr = DB.Column(DB.Unicode)
    nomenclature_label_en = DB.Column(DB.Unicode)
    nomenclature_definition_en = DB.Column(DB.Unicode)
    nomenclature_label_es = DB.Column(DB.Unicode)
    nomenclature_definition_es = DB.Column(DB.Unicode)
    nomenclature_label_de = DB.Column(DB.Unicode)
    nomenclature_definition_de = DB.Column(DB.Unicode)
    nomenclature_label_it = DB.Column(DB.Unicode)
    nomenclature_definition_it = DB.Column(DB.Unicode)
    id_broader = DB.Column(DB.Integer)
    hierarchy = DB.Column(DB.Unicode)
