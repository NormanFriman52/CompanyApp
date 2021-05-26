from CompanyApp.database import db


def check_credentials(username, password):
    collection = db.get_collection("users")
    user = collection.find_one({"username": username, "password": password})
    if user:
        return user
    return {}


def get_users():
    collection = db.get_collection("users")
    users = list(collection.find({}, {"password": 0, "_id": 0, "hash_code": 0, "uid": 0}))
    return users


def get_user(username):
    collection = db.get_collection("users")
    user = collection.find_one({"username": username}, {"password": 0, "_id": 0, "hash_code": 0, "uid": 0})
    return user


def set_user_status(username, status):
    collection = db.get_collection("users")
    collection.update_one({'username': username}, {'$set': {"state.available": status}})


def get_last_uid():
    collection = db.get_collection("users")
    assignment_id = collection.find_one({}, {"uid": 1}, sort=[("uid", -1)])
    return assignment_id['uid']
