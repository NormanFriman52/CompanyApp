from flask import Flask
from flask_socketio import SocketIO
from CompanyApp.api import api_bp
from CompanyApp.main import main_bp
from CompanyApp.main_board import main_board_bp
from CompanyApp.authorization import authorization_bp
from CompanyApp.config import Config

app = Flask(__name__)

app.config.from_object(Config)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

app.register_blueprint(main_bp)
app.register_blueprint(api_bp, url_prefix="/api")
app.register_blueprint(main_board_bp, url_prefix="/board")
app.register_blueprint(authorization_bp, url_prefix="/authorization")

socketio = SocketIO(app, cors_allowed_origins="*")
from CompanyApp.api import sockets

socketio.run(app, debug=True)
