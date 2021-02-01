
from flask_sqlalchemy import SQLAlchemy

try:
    from geonature.utils.env import DB
except ImportError:
    DB = SQLAlchemy()
