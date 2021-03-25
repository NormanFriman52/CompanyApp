from CompanyApp.controllers.main_board_messages_controller import get_messages
import json


def get_json(json_path):
    try:
        with open(json_path) as json_file:
            data = json.load(json_file)
        return data
    except Exception:
        return {}


def get_users_params(parse=True):
    users = get_json(r'C:\Users\kgolonka\Desktop\home\ChatApp\CompanyApp\app\CompanyApp\DB\user_structure.json')
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


def get_main_board_massages():
    return {"messages": get_messages()}
