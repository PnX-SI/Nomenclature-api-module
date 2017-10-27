# coding: utf8
from __future__ import (unicode_literals, print_function,
                        absolute_import, division)

from flask import Blueprint, request
from flask_sqlalchemy import SQLAlchemy

from .models import VNomenclatureTaxonomie, TNomenclatures, BibNomenclaturesTypes
from .utils import json_resp

db = SQLAlchemy()

routes = Blueprint('nomenclatures', __name__)


@routes.route('/nomenclature/<int:idType>', methods=['GET'])
@json_resp
def getNomenclatureByTypeAndTaxonomy(idType):
    """
        Route : liste des termes d'une nomenclature
        Possibilité de filtrer par regne et group2Inpn
    """
    regne = request.args.get('regne')
    group2Inpn = request.args.get('group2_inpn')

    response = queryAndFormatNomenclature(idType, regne, group2Inpn)
    if (not response):
        return {'message': 'Nomenclature not found'}, 404
    return response


@routes.route('/nomenclatures', methods=['GET'])
@json_resp
def getNomenclaturesByTypeListAndTaxonomy():
    """
        Route : liste des termes d'un ensemble de nomenclatures
        Possibilité de filtrer par regne et group2Inpn
    """
    regne = request.args.get('regne')
    group2Inpn = request.args.get('group2_inpn')
    types = request.args.getlist('id_type')

    results = []
    for idType in types:
        response = queryAndFormatNomenclature(idType, regne, group2Inpn)
        if response:
            results.append(response)

    if results:
        return results
    return {'message': 'not found'}, 404


def queryAndFormatNomenclature(idType, regne, group2Inpn):
    nomenclature = db.session.query(BibNomenclaturesTypes)\
        .filter_by(id_type=idType).first()
    if (not nomenclature):
        return None

    # Terme de nomenclatures
    q = db.session.query(TNomenclatures)\
        .filter_by(id_type=idType)\
        .filter_by(active=True)

    if regne:
        q = q.join(
            VNomenclatureTaxonomie,
            VNomenclatureTaxonomie.id_nomenclature ==
            TNomenclatures.id_nomenclature
        ).filter(VNomenclatureTaxonomie.regne.in_(('all', regne)))
        if group2Inpn:
            q = q.filter(
                VNomenclatureTaxonomie.group2_inpn.in_(('all', group2Inpn))
            )
    data = q.all()

    response = nomenclature.as_dict()
    if data:
        response["values"] = [n.as_dict() for n in data]
    return response
