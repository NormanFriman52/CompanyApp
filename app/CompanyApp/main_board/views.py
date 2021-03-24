from flask import Blueprint, render_template, url_for, session, request

main_board_bp = Blueprint("main_board", __name__, template_folder="templates")


@main_board_bp.route("/")
def index():
    return render_template("main_board/board.html")
