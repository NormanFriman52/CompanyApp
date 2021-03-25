from CompanyApp.database import db


def get_messages():
    collection = db.get_collection("main_board")
    messages = collection.find({}, {'_id': 0})
    if messages:
        return list(messages)
    else:
        return []


def insert_message(message):
    collection = db.get_collection("main_board")
    collection.insert_one(message)
