from CompanyApp.database import db


def check_credentials(username, password):
    collection = db.get_collection("users")
    user = collection.find_one({"username": username, "password": password})
    if user:
        return user
    return {}


def get_users():
    collection = db.get_collection("users")
    users = list(collection.find({}, {'_id': 0}))
    return users


def set_user_status(username, status):
    collection = db.get_collection("users")
    collection.update_one({'username': username}, {'$set': {"state.available": status}})
