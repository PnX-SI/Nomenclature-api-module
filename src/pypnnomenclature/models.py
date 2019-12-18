
# coding: utf8
from __future__ import (unicode_literals, print_function,
                        absolute_import, division)
from importlib import import_module
from flask import current_app
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import select, func
from utils_flask_sqla.serializers import serializable

# get or create the SQLAlchemy DB instance
DB = current_app.config.get('DB', import_module('.env', 'pypnnomenclature').DB)
@serializable
class CorTaxrefNomenclature(DB.Model):
    """
        Relation entre taxonomie et nomenclature.
        A n'utiliser uniquement lorsque que l'extension 'taxonomie' des nomenclatures est installée
    """
    __tablename__ = 'cor_taxref_nomenclature'
    __table_args__ = {'schema': 'ref_nomenclatures'}
    id_nomenclature = DB.Column(
        DB.Integer,
        ForeignKey('ref_nomenclatures.t_nomenclatures.id_nomenclature'),
        primary_key=True
    )
    regne = DB.Column(DB.Unicode, primary_key=True)
    group2_inpn = DB.Column(DB.Unicode, primary_key=True)


@serializable
class TNomenclatures(DB.Model):
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

    @staticmethod
    def get_default_nomenclature(mnemonique, id_organism=0):
        q = select([
            func.ref_nomenclatures.get_default_nomenclature_value(
                mnemonique, id_organism
            ).label('default')
        ])
        result = DB.session.execute(q)
        return result.fetchone()['default']


class TNomenclatureTaxonomy(TNomenclatures):
    """
    Hérite de TNomenclatures, rajoute une relation vers CorTaxrefNomenclature
    """
    taxref = relationship(
        'CorTaxrefNomenclature',
        lazy='joined'
    )


@serializable
class BibNomenclaturesTypes(DB.Model):
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

    def __repr__(self):
        return self.label_default

    @staticmethod
    def get_default_nomenclature(mnemonique, id_organism=0):
        q = select([
            func.ref_nomenclatures.get_default_nomenclature_value(
                mnemonique, id_organism
            ).label('default')
        ])
        result = DB.session.execute(q)
        return result.fetchone()['default']


class BibNomenclaturesTypeTaxo(BibNomenclaturesTypes):
    '''
    Hérite de BibNomenclaturesTypes, rajoute simplement une relation vers 'nomenclature' avec la jointure vers la taxonomie
    '''
    nomenclatures = relationship(
        'TNomenclatureTaxonomy',
        primaryjoin='and_(TNomenclatureTaxonomy.id_type == BibNomenclaturesTypes.id_type, TNomenclatureTaxonomy.active == True)',
        lazy='joined',
        order_by='TNomenclatureTaxonomy.hierarchy',
    )


# Modèle utilisé seulement si l'extension 'taxonomie'
# du module est activée et installée
@serializable
class VNomenclatureTaxonomie(DB.Model):
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


# Model for Admin
class BibNomenclaturesTypesAdmin(BibNomenclaturesTypes):
    __tablename__ = 'bib_nomenclatures_types'
    __table_args__ = {
        'schema': 'ref_nomenclatures',
        'extend_existing': True
    }
    nomenclature_items = relationship("TNomenclaturesAdmin")


class TNomenclaturesAdmin(TNomenclatures):
    __tablename__ = 't_nomenclatures'
    __table_args__ = {
        'schema': 'ref_nomenclatures',
        'extend_existing': True
    }
    nomenclature_type_name = relationship(
        "BibNomenclaturesTypesAdmin",
        back_populates="nomenclature_items"
    )
