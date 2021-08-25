"""Configurations"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig():
    APPLICATION_ROOT = None
    DEBUG = True
    SECRET_KEY = 'hakunamatata'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    DEBUG = False
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://')


class DevelopmentConfig(BaseConfig):
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI =  'sqlite:///' + os.path.join(basedir, 'fliq.db')
