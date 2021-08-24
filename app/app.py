from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def register_routes(app):
    from routes import app_blueprint
    app.register_blueprint(app_blueprint)

    from api.api import api_blueprint
    app.register_blueprint(api_blueprint)


def create_flask_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    print(app.config)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from database import models
        register_routes(app)


    return app
