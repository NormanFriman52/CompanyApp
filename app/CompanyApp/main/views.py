"""
Module initialize blueprint for main view and create route for '/'.
"""
from flask import Blueprint, render_template, url_for, session,redirect

main_bp = Blueprint("main", __name__, template_folder="templates")


@main_bp.route("/")
def index():
    """
    Redirect to main board if user is logged in and if not it render the index.html template.
    :return: rendered template or url for main_bord
    """
    if session.get('username'):
        return redirect(url_for('main_board.index'))
    return render_template("main/index.html")
