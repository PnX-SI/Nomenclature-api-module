from pathlib import Path
from itertools import chain
from pkg_resources import iter_entry_points

from flask import Flask
from flask_migrate import Migrate

from pypnnomenclature.env import db, ma
from pypnnomenclature.routes import routes


migrate = Migrate()


@migrate.configure
def configure_alembic(alembic_config):
    version_locations = alembic_config.get_main_option("version_locations", default="").split()
    for entry_point in chain(iter_entry_points("alembic", "migrations")):
        _, migrations = str(entry_point).split("=", 1)
        version_locations += [migrations.strip()]
    alembic_config.set_main_option("version_locations", " ".join(version_locations))
    return alembic_config


def create_app():
    app = Flask(__name__)
    app.config.from_envvar("NOMENCLATURE_SETTINGS")
    ma.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db, directory=Path(__file__).parent / "migrations")
    app.register_blueprint(routes, url_prefix="/nomenclatures")
    # TODO admin
    return app
