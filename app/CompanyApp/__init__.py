from flask import Flask
from .api import api_bp
from .main import main_bp
from .main_board import main_board_bp
from .authorization import authorization_bp
from flask_mongoengine import MongoEngine
from CompanyApp.config import Config


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(main_board_bp, url_prefix="/board")
    app.register_blueprint(authorization_bp, url_prefix="/authorization")

    return app
