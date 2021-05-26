"""
Module initialize blueprint for main_board view and create route for '/'.
"""
from flask import Blueprint, render_template, url_for
from CompanyApp.main_board.forms import MessageForm

main_board_bp = Blueprint("main_board", __name__, template_folder="templates")


@main_board_bp.route("/")
def index():
    """
    Create route for / and render template with parameters.
    :return: render template of board.html
    """
    return render_template("main_board/board.html", url_for_api_messages=url_for('api.main_board'), limit=10,
                           message_form=MessageForm())
