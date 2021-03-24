from flask import Flask
from .api import api_bp
from .main import main_bp
from .main_board import main_board_bp


def create_app():
    app = Flask(__name__)

    app.secret_key = "\xb6\x87\n\x10\x8cI0\xc1n\x0c\xf3s\x8f\xd8#\xa5X\x91:\xdd5\x80\xc6\xa6"
    app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(main_board_bp, url_prefix="/board")

    return app
