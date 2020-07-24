import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
          SECRET_KEY = os.environ.get('SECRET_KEY') or 'unicleSafe'
          SQLALCHEMY_DATABASE_URI = os.environ.get('DTABASE_URL') or \'sqlite:///' + os.path.join(basedir, 'app.db')
          SQLALCHEMY_TRACK_MODIFICATIONS = Flase