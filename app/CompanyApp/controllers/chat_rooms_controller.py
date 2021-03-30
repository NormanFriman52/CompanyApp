import os
from CompanyApp.database import db
from CompanyApp.config import UPLOAD_FOLDER
from pymongo import DESCENDING


def get_messages_with_id_lesser(messages, last_id):
    parsed_messages_list = []
    for message in messages:
        if message['msgId'] < last_id:
            parsed_messages_list.append(message)
    return parsed_messages_list


def get_room_messages(participants, limit=None, last_id=None):
    collection = db.get_collection("chat_rooms")
    room = collection.find_one({"participants": participants}, {"_id": 0, })
    if not room:
        create_uploads_directory(participants)
        collection.insert_one({"participants": participants, "lastMsgId": 1, "messages": []})
    messages = sorted(room['messages'], key=lambda k: k['msgId'], reverse=True)

    if last_id:
        messages = get_messages_with_id_lesser(messages, last_id)
        if limit:
            return messages[0:limit]
        return messages
    if limit:
        messages = messages[0:limit]
        return sorted(messages, key=lambda k: k['msgId'])
    return messages


def insert_message_to_room(participants, last_id, message):
    collection = db.get_collection("chat_rooms")
    collection.update_one({'participants': participants},
                          {'$push': {'messages': message}, '$set': {"lastMsgId": last_id + 1}})


def get_last_msg_id_from_room(participants):
    collection = db.get_collection("chat_rooms")
    room_info = collection.find_one({'participants': participants}, {"messages": 0, "_id": 0})
    last_msg_id = room_info['lastMsgId']
    return last_msg_id


def create_uploads_directory(participants):
    directory = participants[0] + '_'+participants[1]
    path = os.path.join(UPLOAD_FOLDER, directory)
    os.makedirs(path)
