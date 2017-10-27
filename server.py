# coding: utf8
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import importlib
import datetime

db = SQLAlchemy()
app_globals = {}


def init_app():
    if app_globals.get('app', False):
        app = app_globals['app']
    else:
        app = Flask(__name__)

    app.config.from_pyfile('config.py')
    db.init_app(app)

    from routes import routes
    app.register_blueprint(routes, url_prefix='/')

    return app


app = init_app()
if __name__ == '__main__':
    app.run()
