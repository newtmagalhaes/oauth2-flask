from ..db import db
from ..models.user import User


def create_user(data: dict):
    new_user = User(**data)

    db.session.add(new_user)
    db.session.commit()

    return new_user
