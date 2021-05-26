from CompanyApp.database import db
from CompanyApp.controllers.users_controller import get_last_uid


def insert_assignment(first_name, last_name, email):
    collection = db.get_collection("assignments")
    assignment_id = get_last_assignment_id() + 1
    collection.insert_one({"first_name": first_name, "last_name": last_name, "email": email, "id": assignment_id})


def get_all_assignments():
    collection = db.get_collection("assignments")
    assignments = collection.find({}, {"_id": 0})
    return list(assignments)


def get_last_assignment_id():
    collection = db.get_collection("assignments")
    assignment_id = collection.find_one({}, {"id": 1}, sort=[("id", -1)])
    if not assignment_id:
        return 0
    return assignment_id['id']


def delete_assignment(assignment_id):
    collection = db.get_collection("assignments")
    collection.remove({"id": assignment_id})


def insert_new_user(user_info):
    collection = db.get_collection("users")
    user_info['state'] = {"online": False, "available": False}
    user_info['uid'] = get_last_uid() + 1
    collection.insert_one(user_info)
