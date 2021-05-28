"""
Module contains the function which operate on assignments collection in database.
"""
from CompanyApp.database import db
from CompanyApp.controllers.users_controller import get_last_uid


def insert_assignment(first_name, last_name, email):
    """
    Function inserts assignment to assignments collection.
    :param first_name: first name
    :param last_name: last name
    :param email: email
    :return: None
    """
    collection = db.get_collection("assignments")
    assignment_id = get_last_assignment_id() + 1
    collection.insert_one({"first_name": first_name, "last_name": last_name, "email": email, "id": assignment_id})


def get_all_assignments():
    """
    Function gets all the assignments from the assignments collection.
    :return:  list of assignments
    """
    collection = db.get_collection("assignments")
    assignments = collection.find({}, {"_id": 0})
    return list(assignments)


def get_last_assignment_id():
    """
    Function gets the last id of assignment in the assignments collection.
    :return: id of last assignment
    """
    collection = db.get_collection("assignments")
    assignment_id = collection.find_one({}, {"id": 1}, sort=[("id", -1)])
    if not assignment_id:
        return 0
    return assignment_id['id']


def delete_assignment(assignment_id):
    """
    Function remove assignment from assignment collection.
    :param assignment_id: id of assignment to be removed.
    :return: None
    """
    collection = db.get_collection("assignments")
    collection.remove({"id": assignment_id})


def insert_new_user(user_info):
    """
    Function insert user into users collection.
    :param user_info: dictionary with user data
    :return: None
    """
    collection = db.get_collection("users")
    user_info['state'] = {"online": False, "available": False}
    user_info['uid'] = get_last_uid() + 1
    collection.insert_one(user_info)
