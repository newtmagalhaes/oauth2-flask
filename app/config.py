import os


def _get_required_env(__key: str) -> str:
    if key := os.getenv(__key):
        return key
    raise AttributeError(f"Attribute '{__key}' not found")


class BaseConfig(object):
    # Flask
    FLASK_DEBUG = False
    TESTING = False
    SECRET_KEY = _get_required_env("SECRET_KEY")

    # Flask-RESTX
    RESTX_MASK_SWAGGER = False

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"


class DevConfig(BaseConfig):
    SQLALCHEMY_ECHO = True
    FLASK_DEBUG = True


class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    TESTING = True


class ProdConfig(BaseConfig):
    RESTX_MASK_SWAGGER = True


_MAPPED_CONFIGS: dict[str, BaseConfig] = {
    "dev": DevConfig(),
    "test": TestConfig(),
    "prod": ProdConfig(),
}


def select_config() -> BaseConfig:
    env = _get_required_env("ENV_NAME")
    # TODO: log when no ENV is provided
    if config := _MAPPED_CONFIGS.get(env):
        return config

    # TODO: log invalid ENV
    return DevConfig()


config = select_config()
print(f"selected config: {config.__dict__}")
