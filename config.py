class Config(object):
    DEBUG = True
    TESTING = False
    SECRET_KEY = "B\xb2?.\xdf\x9f\xa7m\xf8\x8a%,\xf7\xc4\xfa\x91"

    IMAGE_UPLOADS = "/home/username/app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    IMAGE_UPLOADS = "/home/username/projects/my_app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True

    SESSION_COOKIE_SECURE = False