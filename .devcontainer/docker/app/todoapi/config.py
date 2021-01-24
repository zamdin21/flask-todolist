class Config():
    TODOAPI_CONFIG = "Configured by Config in config.py"
    SQLALCHEMY_DATABASE_URI = "sqlite:///db/todoitems.db"


class DevConfig(Config):
    TODOAPI_CONFIG = "configured by DevConfig in config.py"


class DockerConfig(Config):
    TODOAPI_CONFIG = "configured by DockerConfig in config.py"
