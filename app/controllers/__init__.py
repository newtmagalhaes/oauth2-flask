from flask import Blueprint
from flask_restx import Api

from .hello import hello_ns

blueprint = Blueprint('api', __name__)
api = Api(
    blueprint,
    title="Hello world MVC",
    version="1.0",
    description="API",
    security="apikey",
)

# register namespaces
api.add_namespace(hello_ns, path='/hello')
