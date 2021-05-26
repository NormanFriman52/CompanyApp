from flask import Blueprint, render_template, url_for, session,redirect

main_bp = Blueprint("main", __name__, template_folder="templates")


@main_bp.route("/")
def index():
    if session.get('username'):
        return redirect(url_for('main_board.index'))
    return render_template("main/index.html")
