# coding: utf8
from __future__ import (unicode_literals, print_function,
                        absolute_import, division)

from flask import Blueprint, request
from flask_sqlalchemy import SQLAlchemy

from .models import VNomenclatureTaxonomie, TNomenclatures
from .utils import json_resp

db = SQLAlchemy()

routes = Blueprint('nomenclatures', __name__)

@routes.route('/<int:idType>', methods=['GET'])
@json_resp
def getNomenclatureByTypeAndTaxonomy(idType):
    regne = request.args.get('regne')
    group2Inpn = request.args.get('group2_inpn')

    q = db.session.query(TNomenclatures)\
        .filter_by(id_type = idType)

    if regne :
        q = q.join(VNomenclatureTaxonomie, VNomenclatureTaxonomie.id_nomenclature == TNomenclatures.id_nomenclature)\
            .filter(VNomenclatureTaxonomie.regne.in_(('all',regne)))
    if group2Inpn :
        q = q.filter(VNomenclatureTaxonomie.group2_inpn.in_(('group2_inpn',group2Inpn)))
    data = q.all()
    if data:
        return [n.as_dict() for n in data]
    return {'message': 'id_nom not found'}, 404
