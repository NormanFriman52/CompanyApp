from flask import Blueprint, render_template, url_for, session, request, redirect
from CompanyApp.main_board.forms import MessageForm
from CompanyApp.controllers.main_board_messages_controller import insert_message

main_board_bp = Blueprint("main_board", __name__, template_folder="templates")


@main_board_bp.route("/")
def index():
    return render_template("main_board/board.html", url_for_api_messages=url_for('api.main_board'), limit=10,
                           message_form=MessageForm())


@main_board_bp.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        form = MessageForm(request.form)
        if form.validate() and session['username']:
            message = request.form.get("message")
            author = request.form.get("from")
            msg_id = 3
            date = "12.12"
            insert = {
                "body": message,
                "date": date,
                "from": author,
                "msgId": msg_id
            }
            insert_message(insert)
    return redirect(url_for("main_board.index"))
