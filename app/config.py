class Config(object):
    SECRET_KEY = 'ZMLJSZFUVSEPMJMOIDQ8E5CW33MFZ6PQ9BQ7YEW'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    stylesheets = None
    scripts = None
    POSTS_PER_PAGE = 10

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///clima.db'
    DEBUG = False
    CACHE_TYPE = 'simple'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///clima.db'
    DEBUG = True
    ASSETS_DEBUG = True
