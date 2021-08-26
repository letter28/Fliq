from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from constants import STATIC_URL_PATH


def register_routes(app):
    from routes import app_blueprint
    app.register_blueprint(app_blueprint)

    from api.api import api_blueprint
    app.register_blueprint(api_blueprint)


app = Flask(__name__, static_url_path=STATIC_URL_PATH)
app.config.from_object('config.ProductionConfig')
print('App config: ', app.config)

db = SQLAlchemy(app)

with app.app_context():
    import models
    register_routes(app)