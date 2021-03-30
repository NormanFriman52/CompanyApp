from flask import Blueprint, render_template, flash, redirect, session, request, url_for
from .forms import LoginForm
from CompanyApp.controllers.users_controller import check_credentials, set_user_status

authorization_bp = Blueprint("authorization", __name__, template_folder="templates")


@authorization_bp.route("/logout")
def logout():
    set_user_status(session.get('username'), False)
    session.pop('username', None)
    return redirect(url_for("main_board.index"))


@authorization_bp.route("/", methods=["GET", "POST"])
def login():
    if session.get('username'):
        flash(f"You are already logged in", "error")
        return redirect(url_for("main_board.index"))
    form = LoginForm(request.form)

    if request.method == "POST" and form.validate():
        username = request.form.get("user")
        password = request.form.get("password")
        user = check_credentials(username, password)
        if user:
            session["username"] = username
            set_user_status(username, True)
            flash(f"You have successfully logged in as {session.get('username')}.", "success")
        else:
            flash(f"Bad {session.get('username')}.", "success")
            return redirect(url_for("authorization.login"))
        return redirect(url_for("main_board.index"))

    return render_template("authorization/login.html", form=form)
