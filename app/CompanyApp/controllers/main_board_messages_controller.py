from CompanyApp.database import db
import pymongo


def get_messages(limit=None, last_id=None):
    collection = db.get_collection("main_board")
    if last_id:
        if limit:
            return list(collection.find({"msgId": {"$lt": last_id}}, {'_id': 0}).sort("msgId", -1).limit(limit))
        else:
            return list(collection.find({"msgId": {"$lt": last_id}}, {'_id': 0}).sort("msgId", -1))
    if limit:
        return list(collection.find({}, {'_id': 0}).sort("msgId", -1).limit(limit))
    else:
        return list(collection.find({}, {'_id': 0}))


def insert_message(message):
    collection = db.get_collection("main_board")
    collection.insert_one(message)


def get_last_id():
    collection = db.get_collection("main_board")
    collection.find_one()
    last_record = collection.find_one({}, {"_id": False, 'body': False, 'date': False, 'from': False},
                                      sort=[('_id', pymongo.DESCENDING)])

    return last_record['msgId']


