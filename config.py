import os
basedir = os.path.abspath(os.path.dirname(__file__))
#С нашим конфигурационным файлом мы немного позаимствуем настройку конфигурации Django. У нас будет базовый
# конфигурационный класс, на который наследуются другие классы конфигурации. Затем мы импортируем соответствующий
# класс конфигурации по мере необходимости.

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'JlbyIrfaCnjbngjlEukjv$5Uhflecjd'


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