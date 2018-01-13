class Config(object):
    SECRET_KEY = 'YmVybmFyZG8gZSBmb2RhbyBlIHRyYW5zYWRvci4gTmFvIG1leGUgY29tIGVsZQ=='
    WTF_CSRF_ENABLED = False

    PORT = 5000
    DEBUG = False
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "secret"

    with open('version.txt') as stream:
        APP_VERSION = stream.read()


class ProductionConfig(Config):
    PORT = 8001


class StagingConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
