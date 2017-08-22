# coding: utf8
from __future__ import (unicode_literals, print_function,
                        absolute_import, division)

from flask import Blueprint

from .models import TNomenclatures, BibNomenclaturesTypes
from .utils import json_resp

routes = Blueprint('taxonomie', __name__)

@routes.route('/', methods=['GET'])
@json_resp
def getAllNomenclature():
    noms = TNomenclatures.query.all()
    if noms:
        return [n.as_dict() for n in noms]
    return {'message': 'id_nom not found'}, 404
