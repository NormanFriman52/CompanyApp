from flask import Blueprint, render_template, flash, redirect, session, request, url_for
from .forms import LoginForm, RegisterForm
from CompanyApp.controllers.users_controller import check_credentials, set_user_status
from CompanyApp.controllers.registration_controller import insert_assignment, get_all_assignments, delete_assignment, \
    insert_new_user

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


@authorization_bp.route("/register", methods=["POST", "GET"])
def register():
    if session.get('username'):
        flash(f"You are already logged in", "error")
        return redirect(url_for("main_board.index"))

    form = RegisterForm(request.form)

    if request.method == "POST" and form.validate():
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        insert_assignment(first_name, last_name, email)
        flash(f"You have successfully register. Our team will email you with status of you assignment.", "success")
        return redirect(url_for("authorization.register"))
    return render_template("authorization/register.html", form=form)


@authorization_bp.route("/assignments", methods=["POST", "GET"])
def assignment_center():
    if session.get('username') != "kamil":
        return redirect(url_for("main_board.index"))

    assignments = get_all_assignments()
    if request.method == "POST":
        if request.form.get("delete"):
            assignment_id = int(request.form.get("delete"))
            delete_assignment(assignment_id)
            return redirect(url_for("authorization.assignment_center"))
        fields = ["name", "surname", "email", "username", "password", "gender"]
        user_info = {}
        for field in fields:
            if not request.form.get(field):
                return redirect(url_for("authorization.assignment_center"))
            user_info[field] = request.form.get(field)
        insert_new_user(user_info)
        delete_assignment(int(request.form.get('assignment_id')))
        return redirect(url_for("authorization.assignment_center"))
    return render_template("authorization/assignment.html", assignments=assignments)
