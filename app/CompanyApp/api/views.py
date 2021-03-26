from flask import Blueprint, render_template, url_for, session, request, redirect, jsonify
from CompanyApp.data_parser import *
from CompanyApp.controllers.main_board_messages_controller import insert_message, get_last_id
from CompanyApp.main_board.forms import MessageForm
from datetime import datetime

api_bp = Blueprint("api", __name__, template_folder="templates")


@api_bp.route("/")
def index():
    return 'api'


@api_bp.route("/users")
def users():
    uid = request.args.get('uid')
    if uid:
        return get_single_user_params(uid)
    else:
        return get_users_params()


@api_bp.route("/main_board")
def main_board():
    limit = request.args.get("limit")
    last_id = request.args.get("lastId")
    if last_id:
        last_id = int(last_id)
        if limit:
            limit = int(limit)
            return get_main_board_massages(limit=limit, last_id=last_id)

        return get_main_board_massages(last_id=last_id)
    if limit:
        limit = int(limit)
        return get_main_board_massages(limit)
    return get_main_board_massages()


@api_bp.route("/main_board/send", methods=["POST"])
def send():
    payload = request.get_json()
    if session['username']:
        insert_msg = {
            "body": payload.get("message"),
            "date": f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}',
            "from": payload.get("from"),
            "msgId": get_last_id() + 1
        }
        if payload.get("message"):
            insert_message(insert_msg)
        content = {
            "status": "OK"
        }
        resp = jsonify(content)
        resp.status_code = 200
        return resp
