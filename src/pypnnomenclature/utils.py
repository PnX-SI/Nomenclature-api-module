#coding: utf8
from flask_sqlalchemy import SQLAlchemy
from flask import json, Response

from sqlalchemy import inspect
from sqlalchemy.orm import class_mapper, ColumnProperty, RelationshipProperty

from functools import wraps

db = SQLAlchemy()

class serializableModel(db.Model):
    __abstract__ = True
    def as_dict(self, recursif=False):
        obj={}
        for prop in class_mapper(self.__class__).iterate_properties:
            if isinstance(prop, ColumnProperty)  :
                column = self.__table__.columns[prop.key]
                if isinstance(column.type, (db.Date, db.DateTime)) :
                    obj[prop.key] =str(getattr(self, prop.key))
                else :
                    obj[prop.key] =getattr(self, prop.key)
            if ((isinstance(prop,RelationshipProperty)) and (recursif)):
                obj[prop.key] = [d.as_dict(recursif) for d in getattr(self, prop.key)]

        return obj

def json_resp(fn):
    '''
    Décorateur transformant le résultat renvoyé par une vue
    en objet JSON
    '''
    @wraps(fn)
    def _json_resp(*args, **kwargs):
        res = fn(*args, **kwargs)
        if isinstance(res, tuple):
            res, status = res
        else:
            status = 200
        return Response(json.dumps(res),
                status=status, mimetype='application/json')
    return _json_resp
