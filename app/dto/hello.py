from flask_restx import Namespace, fields


class HelloDTO:
    api = Namespace("hello")

    hello = api.model(
        "hello",
        {
            "hello": fields.String(
                default="world",
                description="'world' string"
            ),
        },
    )
