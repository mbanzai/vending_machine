# Generic imports
import os
import logging
from logging.handlers import RotatingFileHandler

# Third-party imports
from flask import Flask

# Local imports
from config import app_config


def create_app(config_name):
    if os.getenv('FLASK_CONFIG') == "production":
        app = Flask(__name__)
        app.config.update(
            SECRET_KEY=os.getenv('SECRET_KEY'),
        )
    else:
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object(app_config[config_name])

    # Logging
    formatter = logging.Formatter("%(asctime)s | %(pathname)s:%(lineno)d | %(funcName)s | %(levelname)s | %(message)s ")
    handler = RotatingFileHandler(app.config['LOG_FILENAME'], maxBytes=100000, backupCount=1)
    handler.setLevel(logging.DEBUG)

    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.INFO)
    log.addHandler(handler)

    # Blueprints
    from .setup import setup as host_blueprint
    app.register_blueprint(host_blueprint)

    return app