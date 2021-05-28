"""
Module contains the function which operate on users collection in database.
"""
from CompanyApp.database import db


def check_credentials(username, password):
    """
    Function check if username collection contains the user with given username and password.
    :param username: username
    :param password: password
    :return: dictionary with user data if the credentials are correct, otherwise empty dictionary
    """
    collection = db.get_collection("users")
    user = collection.find_one({"username": username, "password": password})
    if user:
        return user
    return {}


def get_users():
    """
    Function gets the users data from users collection.
    :return: list of users
    """
    collection = db.get_collection("users")
    users = list(collection.find({}, {"password": 0, "_id": 0, "hash_code": 0, "uid": 0}))
    return users


def get_user(username):
    """
    Function gets the user data from users collection with specified username.
    :param username: name of user
    :return: dictionary with user data
    """
    collection = db.get_collection("users")
    user = collection.find_one({"username": username}, {"password": 0, "_id": 0, "hash_code": 0, "uid": 0})
    return user


def set_user_status(username, status):
    """
    Function set the state.available key to given status.
    :param username: name of user for which the status will be changed
    :param status: status
    :return: None
    """
    collection = db.get_collection("users")
    collection.update_one({'username': username}, {'$set': {"state.available": status}})


def get_last_uid():
    """
    Function returns the last uid from users collection
    :return: last uid
    """
    collection = db.get_collection("users")
    assignment_id = collection.find_one({}, {"uid": 1}, sort=[("uid", -1)])
    return assignment_id['uid']
