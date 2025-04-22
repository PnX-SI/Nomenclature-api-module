from pathlib import Path
from backports.entry_points_selectable import entry_points

from flask import Flask
from flask_migrate import Migrate

from pypnnomenclature.env import db, ma
from pypnnomenclature.routes import routes


migrate = Migrate()


@migrate.configure
def configure_alembic(alembic_config):
    version_locations = alembic_config.get_main_option("version_locations", default="").split()
    for entry_point in entry_points(group="alembic", name="migrations"):
        version_locations += [entry_point.value]
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
