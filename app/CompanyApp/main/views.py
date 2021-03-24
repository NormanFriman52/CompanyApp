from flask import Blueprint, render_template, url_for, session

main_bp = Blueprint("main", __name__, template_folder="templates")


@main_bp.route("/")
def index():
    session["url"] = url_for("main.index")
    return render_template("main/index.html")
