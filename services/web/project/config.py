import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/project/static"
    MEDIA_FOLDER = f"{os.getenv('APP_FOLDER')}/project/media"


# Side-note: We'll store an application secret in ENV (.env files at least and
# probably also in a cloud service for secrets like GCP ConfigMap/Secrets.)
# This can be used with others for signing/securing anything in the app. It must
# never go into a repo and must never be revealed anywhere unintentionally.
# One way to generate a random secret we could use:
# python -c 'import secrets; print(secrets.token_hex())'
#
# Idea: We probably want a distinct .env file just for secrets and will want one
# for different environments etc.
#

# This is a good section to jump to about Flask config. RE the prefix feature
# and including valid json. I think we will use the ENV and not and python/cfg files.
# https://flask.palletsprojects.com/en/2.1.x/config/#configuring-from-environment-variables

# More good tips further down that page:
# https://flask.palletsprojects.com/en/2.1.x/config/#development-production

