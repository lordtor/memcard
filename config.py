import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'JlbyIrfaCnjbngjlEukjv$5Uhflecjd'
    SQLALCHEMY_DATABASE_URI = os.environ['DB_URL']
    #SQLALCHEMY_DATABASE_URI = os.environ['postgres://kljjqtvl:p4i93ExZ70ik9q8QsFzQvHD5MF1gnllb@baasu.db.elephantsql.com:5432/kljjqtvl']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True