"""
This module contains routes for the API endpoints.
"""

import os
import string
import random
from datetime import datetime
from flask import Blueprint, flash, url_for, session, request, redirect, send_from_directory
from CompanyApp.config import *
from CompanyApp.data_parser import *
from CompanyApp.controllers.main_board_messages_controller import insert_message, get_last_id
from CompanyApp.controllers.chat_rooms_controller import insert_message_to_room, get_last_msg_id_from_room

api_bp = Blueprint("api", __name__, template_folder="templates")


@api_bp.route("/users")
def users():
    """
    Create route for /users which is REST API GET endpoint. Endpoint can be used with parameter 'username'.
    Function call other functions which take users data from database and format the data.

    :return: With given parameter 'username' returns single user data with that 'username'
    otherwise returns data about all the users.
    """
    username = request.args.get('username')
    if username:
        return get_single_user_params(username)
    else:
        return get_users_params()


@api_bp.route("/main_board")
def main_board():
    """
    Create route for /main_board which is REST API GET endpoint.
    Endpoint can be used with parameters 'limit' and 'last_id'
    Function call other function which take main_board messages data from database and format the data.
    :return: With given 'limit' parameter returns limited number of messages.
             With given 'last_id' parameter it returns the messages starting from the one with 'last_id' given.
             Otherwise it returns all the messages.
    """
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


@api_bp.route("/chat_rooms")
def chat_rooms():
    """
    Create route for /chat_rooms which is REST API GET endpoint. Endpoint need arguments 'friend' and 'user' to specify
    which data need to be taken from database.
    Endpoint can be used with parameters 'limit', 'last_id'
    Function call other function which take chat_rooms messages data from database and format the data.
    :return: With given 'limit' parameter returns limited number of messages.
             With given 'last_id' parameter it returns the messages starting from the one with 'last_id' given.
             Without 'friend' and 'user' parameters function returns empty dictionary.
             Otherwise it returns all the messages.
    """
    participants = [request.args.get("friend"), request.args.get("user")]
    if None in participants:
        return {}
    limit = request.args.get("limit")
    last_id = request.args.get("lastId")
    participants.sort()
    if last_id:
        last_id = int(last_id)
        if limit:
            limit = int(limit)
            return get_chat_room_messages(participants, limit=limit, last_id=last_id)

        return get_chat_room_messages(participants, last_id=last_id)
    if limit:
        limit = int(limit)
        return get_chat_room_messages(participants, limit)
    return get_chat_room_messages(participants)


@api_bp.route("/main_board/send", methods=["POST"])
def send():
    """
    Create route for /main_board/send. which is REST API POST endpoint.
    Endpoint need the 'user' and 'friend' parameters to specify to which document in database insert the data.
    Endpoint validate the user and json message POSTED and insert the message into database.
    :return: response as empty dictionary
    """
    payload = request.get_json()
    if session['username'] and payload.get("message"):
        insert_msg = {
            "body": payload.get("message"),
            "date": f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}',
            "from": payload.get("from"),
            "attachment": False
        }
        if request.args.get("friend") and request.args.get("user"):
            participants = [request.args.get("friend"), request.args.get("user")]
            participants.sort()
            last_id = get_last_msg_id_from_room(participants) + 1
            insert_msg["msgId"] = last_id
            insert_message_to_room(participants, last_id, insert_msg)
        else:
            insert_msg["msgId"] = get_last_id() + 1
            insert_message(insert_msg)
        return {}


def allowed_file(filename):
    """
    Function validate if file have proper format and extension.
    :param filename: name of the validated file
    :return: true if file is allowed, otherwise false
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@api_bp.route('/upload', methods=['POST'])
def upload_file():
    """
    Create route for /upload which is REST API POST endpoint.
    Endpoint need the 'user' and 'friend' parameters to specify in which directory store the file.
    Endpoint also need file in the request, the file is validated, then the file gets random name
    and it is saved in the directory with all the user and friend files.
    :return: redirect for main_board
    """
    user = request.args.get("user")
    friend = request.args.get("friend")
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            if user and friend:
                participants = [friend, user]
                participants.sort()
                storage_directory = participants[0] + "_" + participants[1]
                storage_directory = (os.path.join(UPLOAD_FOLDER, storage_directory))
                filename = id_generator()
                body = file.filename
                last_id = get_last_msg_id_from_room(participants) + 1

                file_type = file.filename.rsplit('.', 1)[1].lower()
                file.save(os.path.join(storage_directory, filename + '.' + file_type))

                insert_msg = {
                    "body": body,
                    "date": f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}',
                    "from": user,
                    "attachment": {"type": file_type,
                                   "file_name": filename},
                    "msgId": last_id
                }
                insert_message_to_room(participants, last_id, insert_msg)

            else:
                filename = id_generator()
                body = file.filename
                storage_directory = (os.path.join(UPLOAD_FOLDER, "main"))
                file_type = file.filename.rsplit('.', 1)[1].lower()
                file.save(os.path.join(storage_directory, filename + '.' + file_type))
                insert_msg = {
                    "body": body,
                    "date": f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}',
                    "from": user,
                    "attachment": {"type": file_type,
                                   "file_name": filename},
                    "msgId": get_last_id() + 1
                }
                insert_message(insert_msg)

            return redirect(url_for('main_board.index'))


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    """
    Generate random sequence of characters.
    :param size: size of the sequence, default is 6
    :param chars: specification of the type of characters, default is uppercase letters and digits.
    :return: generated sequence
    """
    return ''.join(random.choice(chars) for _ in range(size))


@api_bp.route('/uploads/')
@api_bp.route('/uploads/<filename>')
@api_bp.route('/uploads/<path>/<filename>')
def uploaded_file(filename=None, path=None):
    """
    Returns the full path with the config UPLOAD FOLDER path, directory and filename
    :param filename: name of the file
    :param path: name of the directory where the files are stored
    :return: full path to file
    """
    if path:
        directory = os.path.join(UPLOAD_FOLDER, path)
    else:
        directory = UPLOAD_FOLDER
    return send_from_directory(directory, filename)
