# coding: utf8
from __future__ import (unicode_literals, print_function,
                        absolute_import, division)

from flask import Blueprint, request
from flask_sqlalchemy import SQLAlchemy

from .repository import get_nomenclature_list
from .utils import json_resp


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

    response = get_nomenclature_list(idType, regne, group2Inpn)
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
        response = get_nomenclature_list(idType, regne, group2Inpn)
        if response:
            results.append(response)

    if results:
        return results
    return {'message': 'not found'}, 404
