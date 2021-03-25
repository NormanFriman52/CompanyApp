from flask import Blueprint, render_template, url_for, session, request, redirect
from CompanyApp.main_board.forms import MessageForm

main_board_bp = Blueprint("main_board", __name__, template_folder="templates")


@main_board_bp.route("/")
def index():
    return render_template("main_board/board.html", url_for_api_messages=url_for('api.main_board'),
                           message_form=MessageForm())


@main_board_bp.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        form = MessageForm(request.form)
        print(request.form.get("message"))

    return redirect(url_for("main_board.index"))
