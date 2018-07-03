# coding: utf8
from flask import Flask, request
from flask_admin import Admin
import importlib
import datetime
from src.pypnnomenclature.env import DB
app_globals = {}


def init_app():
    if app_globals.get('app', False):
        app = app_globals['app']
    else:
        app = Flask(__name__)
    app.config.from_pyfile('config.py')
    DB.init_app(app)

    from routes import routes
    app.register_blueprint(routes, url_prefix='/')

    # import admin
    with app.app_context():
        from admin import *
    return app


app = init_app()
if __name__ == '__main__':
    app.run()
