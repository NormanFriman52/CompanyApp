from CompanyApp.database import db
import pymongo


def get_messages(limit=None):
    collection = db.get_collection("main_board")
    if limit:
        messages = collection.find({}, {'_id': 0}).sort("msgId", -1).limit(limit)
    else:
        messages = collection.find({}, {'_id': 0})
    if messages:
        return list(messages)
    else:
        return []


def insert_message(message):
    collection = db.get_collection("main_board")
    collection.insert_one(message)


def get_last_id():
    collection = db.get_collection("main_board")
    collection.find_one()
    last_record = collection.find_one({}, {"_id": False, 'body': False, 'date': False, 'from': False},
                                      sort=[('_id', pymongo.DESCENDING)])

    return last_record['msgId']

