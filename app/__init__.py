from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from .config import config
from .controllers import blueprint as api
from .db import db

cors = CORS()
migrate = Migrate()


def create_app() -> Flask:
    app = Flask(__name__)

    app.config.from_object(config)
    app.register_blueprint(api)

    # Register extensions
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # with app.app_context():
    #     db.create_all()

    return app
