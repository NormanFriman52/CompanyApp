"""
Module contains the function which operate on main_board collection in database.
"""
from CompanyApp.database import db
from pymongo import DESCENDING


def get_messages(limit=None, last_id=None):
    """
    Function gets the main_board collection data from database.
    :param limit: value by which the number of messages will be limited. Default is None
    :param last_id: value by which massages will be filtered. Default is None
    :return: list of messages
    """
    collection = db.get_collection("main_board")
    if last_id:
        if limit:
            return list(collection.find({"msgId": {"$lt": last_id}}, {'_id': 0}).sort("msgId", -1).limit(limit))
        else:
            return list(collection.find({"msgId": {"$lt": last_id}}, {'_id': 0}).sort("msgId", -1))
    if limit:
        messages = list(collection.find({}, {'_id': 0}).sort("msgId", -1).limit(limit))
        messages = sorted(messages, key=lambda k: k['msgId'])
        return messages
    else:
        return list(collection.find({}, {'_id': 0}))


def insert_message(message):
    """
    Function insert data to main_board collection in database.
    :param message: dictionary with message data
    :return: None
    """
    collection = db.get_collection("main_board")
    collection.insert_one(message)


def get_last_id():
    """
    Function gets the last id of the message in main_board collection.
    :return: last id of message
    """
    collection = db.get_collection("main_board")
    collection.find_one()
    last_record = collection.find_one({}, {"_id": False, 'body': False, 'date': False, 'from': False},
                                      sort=[('_id', DESCENDING)])

    return last_record['msgId']


