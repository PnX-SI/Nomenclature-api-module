# coding: utf8
from __future__ import (unicode_literals, print_function,
                        absolute_import, division)

from flask import Blueprint, request

from .repository import get_nomenclature_list
from .utils import json_resp


routes = Blueprint('nomenclatures', __name__)



@routes.route('/nomenclature/<int:id_type>', methods=['GET'])
@json_resp
def get_nomenclature_by_type_and_taxonomy(id_type):
    """
        Route : liste des termes d'une nomenclature
        Possibilité de filtrer par regne et group2Inpn
    """
    regne = request.args.get('regne')
    group2inpn = request.args.get('group2_inpn')

    response = get_nomenclature_list(
        id_type,
        regne,
        group2inpn,
        filter_params=request.args
    )
    if (not response):
        return {'message': 'Nomenclature not found'}, 404
    return response


@routes.route('/nomenclatures', methods=['GET'])
@json_resp
def get_nomenclature_by_type_list_and_taxonomy():
    """
        Route : liste des termes d'un ensemble de nomenclatures
        Possibilité de filtrer par regne et group2Inpn
    """
    regne = request.args.get('regne')
    group2inpn = request.args.get('group2_inpn')
    types = request.args.getlist('id_type')

    results = []
    for id_type in types:
        response = get_nomenclature_list(
            id_type,
            regne,
            group2inpn,
            filter_params=request.args
        )
        if response:
            results.append(response)

    if results:
        return results
    return {'message': 'not found'}, 404
