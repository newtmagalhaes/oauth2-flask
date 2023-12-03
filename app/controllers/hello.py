from flask_restx import Resource

from ..dto.hello import HelloDTO

hello_ns = HelloDTO.api
_hello = HelloDTO.hello


@hello_ns.route("/")
class Hello(Resource):
    @hello_ns.marshal_with(_hello)
    def get(self):
        """Hello world"""
        return {"hello": "world"}, 200
