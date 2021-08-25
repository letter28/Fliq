"""Configurations"""
import os


class BaseConfig():
    DEBUG = True
    SECRET_KEY = 'hakunamatata'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    DEBUG = False
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class DevelopmentConfig(BaseConfig):
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///fliq.db'
