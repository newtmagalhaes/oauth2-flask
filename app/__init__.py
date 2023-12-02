from flask import Flask
from flask_cors import CORS

from .controller import blueprint as api

cors = CORS()


def create_app() -> Flask:
    app = Flask(__name__)

    # TODO: add config
    app.register_blueprint(api)

    # Register extensions
    cors.init_app(app)

    return app
