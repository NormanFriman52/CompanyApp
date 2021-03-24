from flask import Blueprint, render_template, url_for, session, request
from CompanyApp.data_parser import *

api_bp = Blueprint("api", __name__, template_folder="templates")


@api_bp.route("/")
def api():
    return 'api'


@api_bp.route("/users")
def user():
    uid = request.args.get('uid')
    if uid:
        return get_single_user_params(uid)
    else:
        return get_users_params()
