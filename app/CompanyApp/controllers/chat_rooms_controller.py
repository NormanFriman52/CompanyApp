"""
Module contains the function which operate on chat rooms collection in database.
"""
import os
from CompanyApp.database import db
from CompanyApp.config import UPLOAD_FOLDER


def get_messages_with_id_lesser(messages, last_id):
    """
    Filter the list of messages by the 'msgID' key lesser than last_id parameter.
    :param messages: list of message to filter
    :param last_id: value by which massages will be filtered
    :return: filtered list of messages
    """
    parsed_messages_list = []
    for message in messages:
        if message['msgId'] < last_id:
            parsed_messages_list.append(message)
    return parsed_messages_list


def get_room_messages(participants, limit=None, last_id=None):
    """
    Get data from chat_rooms collection with given participants list.
    :param participants: list of users
    :param limit: value by which the number of messages will be limited. Default is None
    :param last_id: value by which massages will be filtered. Default is None
    :return: list of messages
    """
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
    """
    Function insert the message to chat_rooms collection.
    :param participants: list of users
    :param last_id: id of last message
    :param message: dictionary with message data
    :return: None
    """
    collection = db.get_collection("chat_rooms")
    collection.update_one({'participants': participants},
                          {'$push': {'messages': message}, '$set': {"lastMsgId": last_id}})


def get_last_msg_id_from_room(participants):
    """
    Function get the last message id from chat_rooms collection document with specified participants.
    :param participants: list of users
    :return: last id
    """
    collection = db.get_collection("chat_rooms")
    room_info = collection.find_one({'participants': participants}, {"messages": 0, "_id": 0})
    last_msg_id = room_info['lastMsgId']
    return last_msg_id


def create_uploads_directory(participants):
    """
    Function creates directory in UPLOAD FOLDER path.
    :param participants: list of users
    :return: None
    """
    directory = participants[0] + '_'+participants[1]
    path = os.path.join(UPLOAD_FOLDER, directory)
    os.makedirs(path)
