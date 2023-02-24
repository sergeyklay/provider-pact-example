# This file is part of the Contract Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

import os


class Config:
    """Base config, uses staging database server."""
    TESTING = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    BASE_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """Uses development database server."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DEV_DATABASE_URL',
        'sqlite:///' + os.path.join(Config.BASE_PATH, 'dev-db.sqlite3')
    )


class TestingConfig(Config):
    """Uses in-memory database server."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL', 'sqlite://')


class ProductionConfig(Config):
    """Uses production database server."""
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'sqlite:///' + os.path.join(Config.BASE_PATH, 'ddb.sqlite3')
    )


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}