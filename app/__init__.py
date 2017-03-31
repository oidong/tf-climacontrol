from flask import Flask, app
from app import models
from .models import db
from app.controllers.main import main_blueprint


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    
    db.init_app(app)

    app.register_blueprint(main_blueprint)

    return app

if __name__ == "__main__":
    app.run()

