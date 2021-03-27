from CompanyApp.controllers.main_board_messages_controller import get_messages
from CompanyApp.controllers.chat_rooms_controller import get_room_messages
from CompanyApp.controllers.users_controller import get_users
import json


def get_json(json_path):
    try:
        with open(json_path) as json_file:
            data = json.load(json_file)
        return data
    except Exception:
        return {}


def get_users_params(parse=True):
    users = get_users()
    if parse:
        return {"users": users}
    return users


def get_single_user_params(uid):
    if isinstance(uid, str):
        uid = int(uid)
    users = get_users_params(parse=False)
    for user in users:
        if user["uid"] == uid:
            return user
    else:
        return {}


def get_main_board_massages(limit=None, last_id=None):
    return {"messages": get_messages(limit=limit, last_id=last_id)}


def get_chat_room_messages(participants, limit=None, last_id=None):
    return {"messages": get_room_messages(participants, limit=limit, last_id=last_id)}
