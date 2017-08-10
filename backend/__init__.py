import os
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

# initialize sql-alchemy
db = SQLAlchemy()

# import config file
from config import app_config
from app.endpoints import bucketlist_blueprint


def create_app(config_name):
    app = FlaskAPI(__name__)
    app.config.from_object(app_config)
    db.init_app(app)
    app.register_blueprint(bucketlist_blueprint)

    return app
