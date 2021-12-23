"""Flask configuration."""
from os import environ, path

class BaseConfig():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 102400 * 102400

class ProdConfig():
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://odbfqtlyzkmqtn:b0176277b79c5454581834ec9fcef7a1f6e67246527aded71bd085afc2a13682@ec2-54-91-188-254.compute-1.amazonaws.com:5432/dcghtqakoogh5i'


class DevConfig():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost/usng"
