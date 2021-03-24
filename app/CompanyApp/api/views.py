from flask import Blueprint, render_template, url_for, session, request

api_bp = Blueprint("api", __name__, template_folder="templates")


@api_bp.route("/")
def api():
    session["url"] = url_for("api.api")
    return 'api'


