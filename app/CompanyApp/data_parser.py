"""
Module for modifying data to different format.
"""

from CompanyApp.controllers.main_board_messages_controller import get_messages
from CompanyApp.controllers.chat_rooms_controller import get_room_messages
from CompanyApp.controllers.users_controller import get_users, get_user
import json


def get_json(json_path):
    """
    # Load and returns the json file from given path.
    :param json_path: path to json file.
    :return: dict with loaded json
    """
    try:
        with open(json_path) as json_file:
            data = json.load(json_file)
        return data
    except Exception:
        return {}


def get_users_params():
    """
    Prepare users data from db to new format.
    :return: dict with
    """
    users = get_users()
    return {"users": users}


def get_single_user_params(username):
    """
    :param username: name of user
    :return: dictionary with user data.
    """
    return get_user(username)


def get_main_board_massages(limit=None, last_id=None):
    """
    Prepare messages data from db to new format.
    :param limit: limit of returned messages
    :param last_id: id of the last message
    :return: return dictionary with 'messages' as key and list of messages as value
    """
    return {"messages": get_messages(limit=limit, last_id=last_id)}


def get_chat_room_messages(participants, limit=None, last_id=None):
    """
    Prepare messages data from db to new format.
    :param participants:
    :param limit:
    :param last_id:
    :return:
    """
    return {"messages": get_room_messages(participants, limit=limit, last_id=last_id)}
