import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/project/static"


# Sidenote: We'll store an application secret in ENV (.env files at least and
# probably also in a cloud service for secrets like GCP ConfigMap/Secrets.)
# This can be used with others for signing/securing anything in the app. It must
# never go into a repo and must never be revealed anywhere.
# One way to generate a random secret:
# python -c 'import secrets; print(secrets.token_hex())'
#
# Idea: We probably want a distinct .env file just for secrets and will want one
# for different environments etc.
#
