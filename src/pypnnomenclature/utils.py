#coding: utf8
from flask_sqlalchemy import SQLAlchemy
from flask import json, Response

from functools import wraps

db = SQLAlchemy()

class serializableModel(db.Model):
    __abstract__ = True

    def as_dict(self, recursif=False):
        return {column.key: getattr(self, column.key)
                if not isinstance(column.type, (db.Date, db.DateTime))
                else json.dumps(getattr(self, column.key))
                for column in self.__table__.columns }


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
