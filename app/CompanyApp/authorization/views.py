from flask import Blueprint, render_template, url_for, session, request
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from .forms import LoginForm

authorization_bp = Blueprint("authorization", __name__, template_folder="templates")


@authorization_bp.route("/", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    return render_template("authorization/login.html", form=form)
